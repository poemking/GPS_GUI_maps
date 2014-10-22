import base64
import Tkinter
import urllib

def getaddress(location, width, height, zoom):
    locationnospaces = urllib.quote_plus(location)
    address = "http://maps.googleapis.com/maps/api/staticmap?\
center={0}&zoom={1}&size={2}x{3}&format=gif&sensor=false"\
.format(locationnospaces, zoom, width, height)
    return address

def getmap(location, width, height, zoom):
    address = getaddress(location, width, height, zoom)
    urlreader = urllib.urlopen(address)
    data = urlreader.read()
    urlreader.close()
    base64data = base64.encodestring(data)
    image = Tkinter.PhotoImage(data=base64data)
    return image

def getlabelname():
    popup = Tkinter.Toplevel()
    popup.title("New marker")
    label = Tkinter.Label(popup, text="Please enter a label for your marker")
    label.pack()
    labelname = Tkinter.StringVar()
    textbox = Tkinter.Entry(popup, textvariable=labelname)
    textbox.pack()
    textbox.focus_force()
    
    button = Tkinter.Button(popup, text="Done", command=popup.destroy)
    button.pack()
    
    popup.wait_window()
    
    text = labelname.get()
    return text

def canvasclick(event):
    x,y = event.x, event.y
    widget = event.widget
    size = 10
    widget.create_oval(x-size, y-size, x+size, y+size, width=2)
    label = getlabelname()
    widget.create_text(x, y+2*size, text=label)

def main():
    location = "22.996346, 120.221674"
    width = 640
    height = 480
    zoom = 18
    window = Tkinter.Tk()
    window.title('NCKU')
    window.minsize(width, height)
    mapimage = getmap(location, width, height, zoom)
    canvas = Tkinter.Canvas(window, width=width, height=height)
    canvas.create_image(0,0,image=mapimage,anchor=Tkinter.NW)
    canvas.bind("<Button-1>", canvasclick)
    canvas.pack()
    state = Tkinter.StringVar()
    checkbutton = Tkinter.Checkbutton(window, text="Button",variable=state, onvalue="checked", offvalue="unchecked")
    checkbutton.pack()
    labelframe = Tkinter.LabelFrame(window, text="LabelFrame")
    button = Tkinter.Button(labelframe, text="Button")
    button.pack()
    labelframe.pack()
    options = Tkinter.StringVar()
    options.set("Option1 Option2 Option3")
    listbox = Tkinter.Listbox(window, listvariable=options)
    listbox.pack()
    listbox.curselection()
    window.mainloop()
if __name__ == "__main__":
    main()