import matplotlib.pyplot as plt
import random

width = 300
height = 400
nb_vertices = 5
random.seed()

x_pts = []
y_pts = []
c_pts = []

xv_axis = []
yv_axis = []
colors = ["red","green","blue","grey","black"]
def distance(x1,y1,x2,y2):
    return abs((x1-x2)+(y1-y2))

def nearest_v(x, y, x_vs, y_vs):
    min_dist = distance(x,y,x_vs[0],y_vs[0])
    ind_n = 0
    for i in range(len(x_vs)):
        d = distance(x,y,x_vs[i],y_vs[i])
        if min_dist < d:
            min_dist = d
            ind_n = i
    return i

for i in range(nb_vertices):
    xv = random.randint(0,width)
    yv = random.randint(0,height)
    xv_axis.append(xv)
    yv_axis.append(yv)

for i in range(width):
    for j in range(height):
        ind = nearest_v(i, j, xv_axis, yv_axis)
        x_pts.append(i)
        y_pts.append(j)
        c_pts.append(colors[ind])
#plt.scatter(xv_axis, yv_axis, c=colors)
fig, ax = plt.subplots()
ax.scatter(xv_axis, yv_axis, c=colors)
ax.scatter(x_pts, y_pts)
plt.show()
