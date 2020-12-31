from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.animation import PillowWriter
import ffmpeg
import math as mt
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 
from celluloid import Camera
from mpl_toolkits.mplot3d import Axes3D

class animation :
    def __init__(self , x_data ,y_data, z_data ):
        self.x1 , self.x2 ,self.x3  = [] , [] ,[]
        self.y1 , self.y2 , self.y3 = [] ,[] ,[]
        self.z1 , self.z2 , self.z3 = [] ,[] ,[]
        for i in range(len(x_data)) :
            self.x1.append([0,x_data[i][0]])
            self.y1.append([0,y_data[i][0]])
            self.z1.append([0,z_data[i][0]])
            self.x2.append([x_data[i][0],x_data[i][1]])
            self.y2.append([y_data[i][0],y_data[i][1]])
            self.z2.append([z_data[i][0],z_data[i][1]])
            self.x3.append([x_data[i][1],x_data[i][2]])
            self.y3.append([y_data[i][1],y_data[i][2]])
            self.z3.append([z_data[i][1],z_data[i][2]])
    def plot_3D(self ):
        fig = plt.figure()
        # camera = Camera(fig)
        axis = plt.axes(projection='3d')
        axis = Axes3D(fig)
        axis.set_xlim3d(-3.3, 3.3)
        axis.set_ylim3d(-3.3, 3.3)
        axis.set_zlim3d(-3.3, 3.3)
        axis.set_xlabel('$X$')
        axis.set_ylabel('$Y$')
        axis.set_zlabel('$Z$')
        axis.set_title("3D simulation")

        line1, = axis.plot([], [],[], lw = 3)  
        line2, = axis.plot([], [],[], lw = 3)  
        line3, = axis.plot([], [],[], lw = 3)  
        po, = axis.plot(0,0,0)
        p1, = axis.plot(0,0,0,'ro')
        p2, = axis.plot(0,0,0,'ro')
        p3, = axis.plot(0,0,0,'bo')

        # for i in range(len(self.x1)):
        def animate(i) :
            p1, = axis.plot(self.x1[i][1],self.y1[i][1],self.z1[i][1],'ro')
            p2, = axis.plot(self.x2[i][1],self.y2[i][1],self.z2[i][1],'ro')
            p3, = axis.plot(self.x3[i][1],self.y3[i][1],self.z3[i][1],'bo')
            line1, = axis.plot(self.x1[i], self.y1[i],self.z1[i],lw = 3) 
            line2, = axis.plot(self.x2[i], self.y2[i],self.z2[i],lw = 3) 
            line3, = axis.plot(self.x3[i], self.y3[i],self.z3[i],lw = 3)
            return line1, line2 , line3 , p1 ,p2 ,p3 ,
   
        anim = FuncAnimation(fig, animate, init_func = None, 
                     frames = len(self.x1), interval = 200, blit = True) 
        plt.show()

    def plot_3D_gif(self ):
        fig = plt.figure()
        camera = Camera(fig)
        axis = plt.axes(projection='3d')
        axis = Axes3D(fig)
        axis.set_xlim3d(-3.3, 3.3)
        axis.set_ylim3d(-3.3, 3.3)
        axis.set_zlim3d(-3.3, 3.3)
        axis.set_xlabel('$X$')
        axis.set_ylabel('$Y$')
        axis.set_zlabel('$Z$')
        axis.set_title("3D simulation")
  
        line1, = axis.plot([], [],[], lw = 3)  
        line2, = axis.plot([], [],[], lw = 3)  
        line3, = axis.plot([], [],[], lw = 3)  
        po, = axis.plot(0,0,0)
        p1, = axis.plot(0,0,0,'ro')
        p2, = axis.plot(0,0,0,'ro')
        p3, = axis.plot(0,0,0,'bo')

        for i in range(len(self.x1)):
            p1, = axis.plot(self.x1[i][1],self.y1[i][1],self.z1[i][1],'ro')
            p2, = axis.plot(self.x2[i][1],self.y2[i][1],self.z2[i][1],'ro')
            p3, = axis.plot(self.x3[i][1],self.y3[i][1],self.z3[i][1],'bo')
            line1, = axis.plot(self.x1[i], self.y1[i],self.z1[i],lw = 3) 
            line2, = axis.plot(self.x2[i], self.y2[i],self.z2[i],lw = 3) 
            line3, = axis.plot(self.x3[i], self.y3[i],self.z3[i],lw = 3)
            camera.snap()

        animation = camera.animate(interval = 200, repeat = False)
                          
        animation.save('3r_testing.gif')

    def plot2d(self ,xx1,xx2,xx3,yy1,yy2,yy3 , axis,fig):
                

        line1, = axis.plot([], [], lw = 3)  
        line2, = axis.plot([], [], lw = 3)  
        line3, = axis.plot([], [], lw = 3)  
        po, = axis.plot(0,0)
        p1, = axis.plot(0,0,'ro')
        p2, = axis.plot(0,0,'ro')
        p3, = axis.plot(0,0,'bo')

        def animate(i): 
            p1.set_data(xx1[i][1],yy1[i][1])
            p2.set_data(xx2[i][1],yy2[i][1])
            p3.set_data(xx3[i][1],yy3[i][1])
            line1.set_data(xx1[i], yy1[i]) 
            line2.set_data(xx2[i], yy2[i]) 
            line3.set_data(xx3[i], yy3[i]) 
            return line1, line2 , line3 , p1 ,p2 ,p3 ,po ,
   
        anim = FuncAnimation(fig, animate, init_func = None, 
                     frames = len(xx1), interval = 200, blit = True) 
        plt.show()

    def plotxy(self):
        fig = plt.figure()  
        
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  
        axis.set_title('XY plane view')
        axis.set_xlabel("X-axis")
        axis.set_ylabel("Y-axis")

        self.plot2d(self.x1,self.x2,self.x3,self.y1,self.y2,self.y3,axis,fig)
    
    def plotxz(self):
        fig = plt.figure()  
        
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  
        axis.set_title('XZ plane view')
        axis.set_xlabel("X-axis")
        axis.set_ylabel("Z-axis")

        self.plot2d(self.x1,self.x2,self.x3,self.z1,self.z2,self.z3,axis,fig)

    def plotyz(self):
        fig = plt.figure()  
        
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  
        axis.set_title('YX plane view')
        axis.set_xlabel("Y-axis")
        axis.set_ylabel("Z-axis")

        self.plot2d(self.y1,self.y2,self.y3,self.z1,self.z2,self.z3,axis,fig)
  
    def planer_gif(self ,xx1 ,xx2 ,xx3 ,yy1, yy2, yy3 , fig ,axis ,camera):
        
        line1, = axis.plot([], [], lw = 3)  
        line2, = axis.plot([], [], lw = 3)  
        line3, = axis.plot([], [], lw = 3)  
        po, = axis.plot(0,0 ,'go')
        p1, = axis.plot(0,0,'ro')
        p2, = axis.plot(0,0,'ro')
        p3, = axis.plot(0,0,'bo')

        for i in range(len(self.x1)):
            po, = axis.plot(0,0 ,'go')
            p1, = axis.plot(xx1[i][1],yy1[i][1],'ro')
            p2, = axis.plot(xx2[i][1],yy2[i][1],'ro')
            p3, = axis.plot(xx3[i][1],yy3[i][1],'bo')
            line1, = axis.plot(xx1[i], yy1[i],lw = 3) 
            line2, = axis.plot(xx2[i], yy2[i],lw = 3) 
            line3, = axis.plot(xx3[i], yy3[i],lw = 3)
            camera.snap()
        
    def xygif(self ):
        fig = plt.figure()
        camera = Camera(fig)
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  

        axis.set_title('XY plane view')
        axis.set_xlabel("X-axis")
        axis.set_ylabel("Y-axis")

        self.planer_gif(self.x1,self.x2,self.x3,self.y1,self.y2,self.y3 ,fig,axis,camera)

        animation_2d = camera.animate(interval = 200, repeat = False)
        animation_2d.save('XY_planer_view.gif')
                 
    def xzgif(self ):
        fig = plt.figure()
        camera = Camera(fig)
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  

        axis.set_title('XZ plane view')
        axis.set_xlabel("X-axis")
        axis.set_ylabel("Z-axis")

        self.planer_gif(self.x1,self.x2,self.x3,self.z1,self.z2,self.z3 ,fig,axis,camera)

        animation_2d = camera.animate(interval = 200, repeat = False)
        animation_2d.save('XZ_planer_view.gif')
                         
    def yzgif(self ):
        fig = plt.figure()
        camera = Camera(fig)
        axis = plt.axes(xlim =(-3.3,3.3),  
                ylim =(-3.3, 3.3))  

        axis.set_title('YZ plane view')
        axis.set_xlabel("Y-axis")
        axis.set_ylabel("Z-axis")

        self.planer_gif(self.y1,self.y2,self.y3,self.z1,self.z2,self.z3 ,fig,axis,camera)

        animation_2d = camera.animate(interval = 200, repeat = False)
        animation_2d.save('YZ_planer_view.gif')
                 

