# User's Yelp API key
api_key = 'Replace with api key'

def data_formatting(data, term):
    import numpy as np
    import pandas as pd
    
    address = []

    # Convert the location from dict to a string
    for i in range(len(data)):    
        address.append(" ".join(data.iloc[i]['location']['display_address']))

    data['location'] = address
    data['category'] = pd.Series(np.zeros(100))
    
    # Extract the main location category out of dict object
    if term == 'takeout':
        for i in range(len(data[['categories']])):
            data['category'].iloc[i] = 'food'
    else:
        for i in range(len(data[['categories']])):
            data['category'].iloc[i] = data[['categories']].iloc[i][0][0]['alias']
        
    if 'price' in data.columns:
        data = data.drop(columns=['alias', 'categories', 'display_phone', 'distance', 'id', 'is_closed', 'transactions', 'price'])
    else:
        data = data.drop(columns=['alias', 'categories', 'display_phone', 'distance', 'id', 'is_closed', 'transactions'])
    
    return data

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
    return data_formatting(data, term)


def pd_to_psql(data, city):
    from sqlalchemy import create_engine, types

    engine = create_engine('postgresql://postgres:password@localhost:5432/city_tour')
    data.to_sql(city, engine, if_exists='replace', dtype = 
                {'coordinates':types.JSON}) 


def selector(db, city, category):
    from random import sample
    from psycopg2 import connect
    
    conn = connect(host='localhost', database=db, user="postgres", password='password')
    cur = conn.cursor()
    
    cur.execute("SELECT index FROM {} WHERE category = '{}';".format(city, category))
    rows = cur.fetchall()[0]
    selection = sample(rows, 1)[0]
    cur.execute('SELECT name, location, phone FROM {} WHERE index = {};'.format(city, selection))
    
    return cur.fetchone()
