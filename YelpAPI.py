# User's Yelp API key
api_key = 'Replace with api key'


def get_yelped(api_key, term, location, total_offset):
    import pandas as pd
    import requests
    
    data = []
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}

    for offset in range(0, total_offset, 50):
        url_params = {
                'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'limit': 50,
                'offset': offset
            }

        response = requests.get(url, headers = headers, params = url_params)
    
        if response.status_code == 200:
            data += response.json()['businesses']
        elif response.status_code == 400:
            print('400 Bad Request')
            break
        
    data = pd.DataFrame.from_dict(data)
    data = data.drop(columns=['alias', 'categories', 'display_phone', 'distance', 'id', 'is_closed', 'transactions'])
    return data_formatting(data)


def data_formatting(data):
    address = []

    for i in range(len(data)):    
        # Converts business location from dict to a string
        address.append(" ".join(data.iloc[i]['location']['display_address']))

    data['location'] = address
    return data


def pd_to_psql(data, table_name):
    from sqlalchemy import create_engine, types

    engine = create_engine('postgresql://postgres:password@localhost:5432/city_tour')
    data.to_sql(table_name, engine, if_exists='replace', dtype = 
                {'coordinates':types.JSON}) 


def selector(db, table):
    from random import randint
    from psycopg2 import connect
    
    conn = connect(host='localhost', database=db, user="postgres", password='password')
    cur = conn.cursor()
    
    cur.execute('SELECT MAX(index) FROM {}'.format(table))
    rowcount = cur.fetchone()[0]
    selection = randint(0, rowcount+1)
    cur.execute('SELECT name, location, phone FROM {} WHERE index = {}'.format(table, selection))
    
    return cur.fetchone()
