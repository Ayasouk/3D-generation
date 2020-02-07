from tkinter import *
import time
from PIL import Image, ImageTk

def create_3d_cube(n):
    x = range(n)
    y = range(n)
    z = range(n)
    cube_points = []
    # Face 1
    for xi in range(0,n):
        for yi in range(0,n):
            cube_points.append(((xi,yi,0), "#ff0000"))
    # Face 2
    for xi in range(0,n):
        for zi in range(0,n):
            cube_points.append(((xi,0,zi),"#00ff00"))
    # Face 3
    for yi in range(0,n):
        for zi in range(0,n):
            cube_points.append(((0,yi,zi),"#0000ff"))
    # Face 4
    for xi in range(0,n):
        for yi in range(0,n):
            cube_points.append(((xi,yi,1),"#555500"))
    # Face 5
    for xi in range(0,n):
        for zi in range(0,n):
            cube_points.append(((xi,1,zi),"#005500"))
    # Face 6
    for yi in range(0,n):
        for zi in range(0,n):
            cube_points.append(((1,yi,zi),"#000055"))

    return cube_points

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master

        self.pack(fill=BOTH, expand=1)
        # BUTTON
        #exitButton = Button(self,text="Exit",command=self.clickExitButton)
        #exitButton.place(x=0,y=0)
        # MENU
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="File",menu=fileMenu)

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit",menu=editMenu)

        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        # CLOCK LABEL
        self.label = Label(self, text = "DOING IT", fg="blue", font=("AR destine", 20))
        self.label.place(x=10,y=10)
        self.update_clock()

        # PYGAME label
        self.label_pygame = Label(self, text = "PY-GAME", fg="blue", font=("AR destine", 20))
        self.label_pygame.place(x=170,y=10)


        # DRAW IMAGE
        self.canvas = Canvas(self,bg="white", height=360,width=380)
        self.canvas.place(x=60,y=50)
        new_img = Image.new("RGBA", (240,180),(0,0,0,255))
        new_img.putpixel((70,60), (255,0,0,255))
        new_img.putpixel((70,61), (255,0,0,255))
        render = ImageTk.PhotoImage(new_img)
        image = self.canvas.create_image(50,50,anchor=NE,image=render)
        
        # IMAGE
        """
        load = Image.open("3D_obj.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)
        """
        
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def exitProgram(self):
        exit()
        
    def clickExitButton(self):
        exit()

        
root = Tk()
app = App(root)
root.wm_title("AR 3DMEDIA")
root.geometry("540x440")
root.after(1000, app.update_clock)
root.mainloop()
