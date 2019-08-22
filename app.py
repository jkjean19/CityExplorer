from tkinter import *
from YelpAPI.yelp import selector


class Start(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.button1 = Button(self, text= 'NYC', command=self.new_york)
        self.button1.pack()
        
        self.button2 = Button(self, text= 'Philadelphia', command=self.phila)
        self.button2.pack()
        
        self.quit_button = Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()
        
        self.pack()
        
    def quit(self):
        self.master.destroy()
        
    def new_york(self):
        self.newWindow = Toplevel(self.master)
        self.app = NYC(self.newWindow)

    def phila(self):
        self.newWindow = Toplevel(self.master)
        self.app = Phila(self.newWindow)
        
        
class City(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):        
        self.master.title("CityTour")
        self.pack()

        self.labelframe = LabelFrame(self, text="Results")
        self.labelframe.pack(fill="both", expand="yes")

        clear_button = Button(self, text="Clear All", command=self.clear)
        clear_button.pack()
        
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.pack()

    def quit(self):
        self.master.destroy()

    def clear(self):
        self.labelframe.destroy()
        self.labelframe = LabelFrame(self, text="Results")
        self.labelframe.pack(fill="both", expand="yes")
            
class NYC(City):

    def init_window(self):
        self.master.title("CityTour")
        self.pack()
        self.header = Label(self, text='New York City', font=('Comic Sans MS',24,'bold'), fg='black').pack()
    
        park_button = Button(self, text="Parks", command=self.park)
        park_button.pack()
        
        
        food_button = Button(self, text="Food Spots", command=self.food)
        food_button.pack()
        
        self.labelframe = LabelFrame(self, text="Results")
        self.labelframe.pack(fill="both", expand="yes")

        clear_button = Button(self, text="Clear All", command=self.clear)
        clear_button.pack()
        
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.pack()
        
        
    def park(self):    
        try:
            park = selector('city_tour', 'new_york_city', 'parks')    
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1] +'\n'+ 
                                             park[2]))
            txt.pack()
        except TypeError:
            park = selector('city_tour', 'new_york_city', 'parks')
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1]))
        
    def food(self):
        try:
            food_spot = selector('city_tour', 'new_york_city', 'food')
            txt = Label(self.labelframe, text= str(food_spot[0] +'\n'+
                                              food_spot[1] +'\n'+ 
                                              food_spot[2]))
            txt.pack()
        except TypeError:
            park = selector('city_tour', 'new_york_city', 'food')
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1]))

            
class Phila(City):

    def init_window(self):
        self.master.title("CityTour")
        self.pack()
        self.header = Label(self, text='Phila', font=('Comic Sans MS',24,'bold'), fg='black').pack()
    
        park_button = Button(self, text="Parks", command=self.park)
        park_button.pack()
        
        food_button = Button(self, text="Food Spots", command=self.food)
        food_button.pack()
        
        self.labelframe = LabelFrame(self, text="Results")
        self.labelframe.pack(fill="both", expand="yes")

        clear_button = Button(self, text="Clear All", command=self.clear)
        clear_button.pack()
        
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.pack()
        
    def park(self):    
        try:
            park = selector('city_tour', 'philadelphia', 'parks')    
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1] +'\n'+ 
                                             park[2]))
            txt.pack()
        except TypeError:
            park = selector('city_tour', 'philadelphia', 'parks')    
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1]))
        
    def food(self):
        try:
            food_spot = selector('city_tour', 'philadelphia', 'food')
            txt = Label(self.labelframe, text= str(food_spot[0] +'\n'+
                                              food_spot[1] +'\n'+ 
                                              food_spot[2]))
            txt.pack()
        except TypeError:
            park = selector('city_tour', 'philadelphia', 'food')    
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1]))

            
window = Tk()
window.geometry("400x300")

app = Start(window)
window.mainloop()  
