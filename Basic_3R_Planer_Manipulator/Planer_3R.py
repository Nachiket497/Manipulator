from Plotter import animation
import numpy as np
import math
x_data , y_data = [ ], [ ]

t1 ,t2 , t3 = 0 , 0 , 0
n = 100
dt = 0.01

for i in range(n):
    t1 += dt
    t2 += dt 
    t3 += dt
    x1 , y1 = np.cos(t1) , np.sin(t1)
    x2 , y2 = x1 + np.cos(t1+t2) , y1 + np.sin(t1+t2)
    x3 , y3 = x2 + np.cos(t1+t2+t3) , y2 + np.sin(t1+t2+t3)
    x_data.append([x1,x2,x3])
    y_data.append([y1,y2,y3])

a = animation(x_data,y_data)
a.plot_2D_gif()





