from tkinter import *
from YelpAPI import selector

class Window(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("CityExplorer")
        self.pack()
        self.header = Label(self, text="CityExplorer", font=("Comic Sans MS",24,"bold"), fg='black').pack()
        
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


    def quit(self):
        exit()
        
        
    def clear(self):
        self.labelframe.destroy()
        self.labelframe = LabelFrame(self, text="Results")
        self.labelframe.pack(fill="both", expand="yes")

        
    def park(self) 
        try:
            park = selector('city_tour', 'parks')    
            txt = Label(self.labelframe, text=str(park[0] +'\n'+ 
                                             park[1] +'\n'+ 
                                             park[2]))
            txt.pack()
        except TypeError:
            pass
    
    
    def food(self):
        try:
            food_spot = selector('city_tour', 'food_spots')
            txt = Label(self.labelframe, text= str(food_spot[0] +'\n'+
                                              food_spot[1] +'\n'+ 
                                              food_spot[2]))
            txt.pack()
        except TypeError:
            pass

        
window = Tk()
window.geometry("400x300")

app = Window(window)
window.mainloop()  
