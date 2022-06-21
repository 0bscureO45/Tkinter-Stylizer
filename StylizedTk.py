from prerequisites import *
from requisites import *
from tkinter import *

class StylizedTk(Tk):
    def __init__(self, render_type, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.render_type = render_type
