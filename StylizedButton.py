from prerequisites import *
from requisites import *
from tkinter import *


class StylizedButton(Label):
    # def __init__(self, master, **kwargs) -> None:
    #     self.master = master
    #     self.config(**kwargs)

    def __init__(self, master, stylized_prop={}, command=None, image=None, **kwargs):
        Label.__init__(self, master, **kwargs)
        if stylized_prop == {}:
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
        self.fontprop = (stylized_prop["font_name"], stylized_prop["font_size"], stylized_prop["font_color"], stylized_prop["font_style"])
        self.command = command
        self.image = PhotoImage(file=rounded_rectangle(width=200,
                                                    height=200,
                                                    radius=100,
                                                    font_prop=self.fontprop,
                                                    fill_color="green",
                                                    border_width=5))
        self.config(image=self.image)
        self.bind('<Button-1>', self.on_click)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self.image = PhotoImage(file=rounded_rectangle(width=200,
                                                    height=200,
                                                    radius=100,
                                                    font_prop=self.fontprop,
                                                    fill_color="red",
                                                    border_width=5))
        self.configure(image=self.image)
        # self.config(bg='#0099CC')

    def on_leave(self, event):
        self.image = PhotoImage(file=rounded_rectangle(width=200,
                                                    height=200,
                                                    radius=100,
                                                    font_prop=self.fontprop,
                                                    fill_color="green",
                                                    border_width=5))
        self.config(image=self.image)
        # self.config(bg='#006699')
        
    def on_click(self, event):
        self.image = PhotoImage(file=rounded_rectangle(width=200,
                                                    height=200,
                                                    radius=100,
                                                    font_prop=self.fontprop,
                                                    fill_color="blue",
                                                    border_width=5))
        self.config(image=self.image)
        self.command()


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x300')
    root.title('Stylized Button')
    root.resizable(False, False)
    test_button = StylizedButton(root, 'Test', command=lambda: print('Test'))
    test_button.pack()
    root.mainloop()
