from prerequisites import *
from requisites import *
from tkinter import *
from StylizedTk import StylizedTk

class StylizedButton(Label):
    def __init__(self, master, stylized_prop={}, command=lambda: print("Button Clicked"), **kwargs):
        Label.__init__(self, master, text="PLACEHOLDER", **kwargs)
        # initializing custom variables
        self.master = master
        self.stylized_prop = stylized_prop
        self.command = command
        # initializing the master type and stylized properties 
        self.type = "pillow"    
        if type(master) is StylizedTk:
            self.type = master.render_type
        if stylized_prop == {}:
            self.master.update()
            stylized_prop = {
                "radius": int(self.winfo_height() / 2),
                "resolution": 5,
                "fill_color": "white",
                "border_color": "darkgreen",
                "border_width": 2,
                "font_name": "comicz.ttf",
                "font_size": 20,
                "font_color": "darkgreen",
                "font_style": "italic"
            }
        
        # initializing the command
        self.bind('<Button-1>', self.command_runner)
        
    def command_runner(self, event):
        self.command()
        
        
#####################################################
#                      TESTING                      #
#####################################################

root = Tk()

stylize_button = StylizedButton(root)
stylize_button.pack()

root.mainloop()