import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.animation import PillowWriter
import ffmpeg
import math as mt
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 
from celluloid import Camera

class animation :
    def __init__(self , x_data ,y_data ):
        self.x1 , self.x2 ,self.x3  = [] , [] ,[]
        self.y1 , self.y2 , self.y3 = [] ,[] ,[]
        for i in range(len(x_data)) :
            self.x1.append([0,x_data[i][0]])
            self.y1.append([0,y_data[i][0]])
            self.x2.append([x_data[i][0],x_data[i][1]])
            self.y2.append([y_data[i][0],y_data[i][1]])
            self.x3.append([x_data[i][1],x_data[i][2]])
            self.y3.append([y_data[i][1],y_data[i][2]])
    
    def plot_2D(self):
        fig = plt.figure()  
        
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  

        axis.set_title('Plane 3R Simulation')
        axis.set_xlabel("X-axis")
        axis.set_ylabel("Y-axis")


        line1, = axis.plot([], [], lw = 3)  
        line2, = axis.plot([], [], lw = 3)  
        line3, = axis.plot([], [], lw = 3)  
        po, = axis.plot(0,0,'go')
        p1, = axis.plot(0,0,'ro')
        p2, = axis.plot(0,0,'ro')
        p3, = axis.plot(0,0,'bo')

        def animate(i): 
            po.set_data(0,0)
            p1.set_data(self.x1[i][1],self.y1[i][1])
            p2.set_data(self.x2[i][1],self.y2[i][1])
            p3.set_data(self.x3[i][1],self.y3[i][1])
            line1.set_data(self.x1[i], self.y1[i]) 
            line2.set_data(self.x2[i], self.y2[i]) 
            line3.set_data(self.x3[i], self.y3[i]) 
            return line1, line2 , line3 , p1 ,p2 ,p3 ,po,
   
        anim = FuncAnimation(fig, animate, init_func = None, 
                     frames = len(self.x1), interval = 200, blit = True) 
        plt.show()

    def plot_2D_gif(self ):
        fig = plt.figure()
        camera = Camera(fig)
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  
  
        axis.set_title('Plane 3R Simulation')
        axis.set_xlabel("X-axis")
        axis.set_ylabel("Y-axis")
        line1, = axis.plot([], [], lw = 3)  
        line2, = axis.plot([], [], lw = 3)  
        line3, = axis.plot([], [], lw = 3)  
        po, = axis.plot(0,0)
        p1, = axis.plot(0,0,'ro')
        p2, = axis.plot(0,0,'ro')
        p3, = axis.plot(0,0,'bo')

        for i in range(len(self.x1)):
            po, = axis.plot(0,0,'go')
            p1, = axis.plot(self.x1[i][1],self.y1[i][1],'ro')
            p2, = axis.plot(self.x2[i][1],self.y2[i][1],'ro')
            p3, = axis.plot(self.x3[i][1],self.y3[i][1],'bo')
            line1, = axis.plot(self.x1[i], self.y1[i],lw = 3) 
            line2, = axis.plot(self.x2[i], self.y2[i],lw = 3) 
            line3, = axis.plot(self.x3[i], self.y3[i],lw = 3)
            camera.snap()

        animation = camera.animate(interval = 200, repeat = False)
                          
        animation.save('3R_planer.gif')

    


