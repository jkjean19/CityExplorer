from tkinter import *
from YelpAPI import selector

def quit():
    exit()
        
def park():    
    park = selector('city_tour', 'parks')    
    txt = Label(labelframe, text=str(park[0] +'\n'+ 
                                     park[1] +'\n'+ 
                                     park[2]))
    txt.pack()
    
def food():
    food_spot = selector('city_tour', 'food_spots')
    txt = Label(labelframe, text= str(food_spot[0] +'\n'+
                                      food_spot[1] +'\n'+ 
                                      food_spot[2]))
    txt.pack()

window = Tk()
window.title("CityTour")
window.geometry("400x300")
header = Label(window, text='CityTour', font=('Comic Sans MS',24,'bold'), fg='black').pack()

park_button = Button(window, text="Parks", command=park)
park_button.pack()

food_button = Button(window, text="Food Spots", command=food)
food_button.pack()

labelframe = LabelFrame(window, text="Results")
labelframe.pack(fill="both", expand="yes")

quit_button = Button(window, text="Quit", command=quit)
quit_button.pack()

window.mainloop()  
