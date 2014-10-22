import Tkinter

window =Tkinter.Tk()

window.title("My maps")
label=Tkinter.Label(window, text="Hello world!")
label.pack()
width=200
height=50
window.minsize(width, height)

window.mainloop()

