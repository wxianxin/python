# python tkinter

# GUIs often use a form of OO programming which we call event-driven: the program responds to events, which are actions that a user takes.
# The window manager is the part of your operating system which handles windows.

# widget classes
Tk(): #  the class which we use to create the root window – the main window of our application. it is possible for us to create other windows which are separate from the main window.
Frame() # a container widget which is placed inside a window, which can have its own border and background – it is used to group related widgets together in an application’s layout.
Toplevel() # a container widget which is displayed as a separate window.
Canvas() # is a widget for drawing graphics. In advanced usage, it can also be used to create custom widgets – because we can draw anything we like inside it, and make it interactive.
Entry() # This widget allows the user to enter one line of text, in a single font. xlsxwriterTo enter multiple lines of text, use the Text widget.
Text() # displays formatted text, which can be editable and can have embedded images.
Button()
Label(): # static element – it doesn’t do anything by default; it just displays something.
Message() # is similar to a Label, but is designed for longer bodies of text which need to be wrapped.
Scrollbar() # allows the user to scroll through content which is too large to be visible all at once.
Checkbutton()
Radiobutton()
Listbox()

Scale() # are different kinds of input widgets – they allow the user to enter information into the program.
Menu()
Menubutton() # are used to create pull-down menus.


# three geometry managers
# We have to use one of the available geometry managers to specify a position for each of our widgets, otherwise the widget will not appear in our window.
pack() # which is one of the three different geometry managers available in tkinter.
grid() # This is the geometry manager recommended for complex interfaces.
place() # allows us to provide explicit sizes and positions for widgets.
self.label.grid(columnspan=2, sticky=W+E)
self.output_path_label.grid(row=2, column=0, sticky=W)
# NOTE Never use both pack and grid inside the same window. The algorithms which they use to calculate widget positions are not compatible with each other, and your program will hang forever as tkinter tries unsuccessfully to create a widget layout which satisfies both of them.

root.geometry('+200+200') # set windows dimension and windows coordinates
root.mainloop(): # is a method on the main window which we execute when we want to run our application. This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console.

class GUI():
    def __init__(self, master):


        self.master = master
        master.title("PIL Setting")
        self.label = Label(master, text="Python-based Incurred Loss calculation engine")
        self.label.grid(row=0, columnspan=3)

        # Radiobutton is grouped by `variable`, difference within the group is the `value`.
        self.var = BooleanVar()
        self.yes = Radiobutton(master, text='yes', variable=self.var, value=1)
        self.no = Radiobutton(master, text='no', variable=self.var, value=0)
        self.var_value = self.var.get()


root = Tk()
my_gui = GUI(root)
root.geometry("+300+400")
root.mainloop()

