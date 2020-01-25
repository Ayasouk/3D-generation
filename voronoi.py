from Tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sqrt
import random
from datetime import datetime

random.seed(datetime.now())

WIDTH, HEIGHT = 640, 480

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
canvas.pack()
img = PhotoImage(width=WIDTH+10, height=HEIGHT+10)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

#for x in range(4 * WIDTH):
#    y = int(HEIGHT/2 + HEIGHT/4 * cos(x/80.0))
#    img.put("#ffffff", (x//4,y))

nb_vertices = 5

x_pts = []
y_pts = []
c_pts = []

xv_axis = []
yv_axis = []
colors = ["#ff0000","#00ff00","#0000ff","#ff00ff","#00ffff"]

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def nearest_v(x, y, x_vs, y_vs):
    min_dist = distance(x,y,x_vs[0],y_vs[0])
    ind_n = 0
    for i in range(1, len(x_vs)):
        d = distance(x,y,x_vs[i],y_vs[i])
        if min_dist < d:
            min_dist = d
            ind_n = i
    return ind_n


for i in range(nb_vertices):
    xv = random.randint(0,WIDTH)
    yv = random.randint(0,HEIGHT)
    xv_axis.append(xv)
    yv_axis.append(yv)
    img.put(colors[i], (xv,yv))


for i in range(WIDTH):
    for j in range(HEIGHT):
        ind = nearest_v(i, j, xv_axis, yv_axis)
        x_pts.append(i)
        y_pts.append(j)
        c_pts.append(ind)
        img.put(colors[ind], (i,j))

mainloop()
