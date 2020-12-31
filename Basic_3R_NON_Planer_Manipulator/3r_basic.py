import numpy as np 
import math as m
import sympy  as sy

class helper():
    def __init__ (self):
        self.id = 0
    @staticmethod 
    def sym_transform(a ,alpha, d , theta):
        T = sy.Matrix([ [ sy.cos(theta)              , -1*sy.sin(theta)           ,      0          ,    a              ],
                        [ sy.sin(theta)*sy.cos(alpha) , sy.cos(theta)*sy.cos(alpha) , -1*sy.sin(alpha) , -1*sy.sin(alpha)*d ],
                        [ sy.sin(theta)*sy.sin(alpha) , sy.cos(theta)*sy.sin(alpha) ,    sy.cos(alpha) ,    sy.cos(alpha)*d ],
                        [ 0                         , 0                         ,    0            ,  1                ]])
        return T
#defining the symbols for angles
theta1 = sy.Symbol('theta1')
theta2 = sy.Symbol('theta2')
theta3 = sy.Symbol('theta3')

#defining the symbols for length of links
Length_link_1 = sy.Symbol('L1')
Length_link_2 = sy.Symbol('L2')
Length_link_3 = sy.Symbol('L3')


#defining the D_H parameter matrix
D_H_parametrs = sy.Matrix([[0,0,0,theta1],[Length_link_1,-90,0,theta2],[Length_link_2,-90,0,theta3] , [0,0,Length_link_3,0]])

#calculating the transformation

# from frame zero to frame 1
T01 = helper.sym_transform(0,0,0,theta1)

# from frame 1 to frame 2
T12 = helper.sym_transform(Length_link_1,sy.pi/2,0,theta2).evalf()

# from frame 2 to frame 3
T23 = helper.sym_transform(Length_link_2,sy.pi/2,0,theta3).evalf()

# from frame 3 to frame 4 ( end effector frame)
T34 = helper.sym_transform(Length_link_3,0,0,0).evalf()

# from frame zero to frame 2
T02 = T01*T12

# from frame zero to frame 3
T03 = T02*T23

# from frame zero to frame 4
T04 = T03*T34

# calculating the positions of endeffector and joint
position_end_effector = T04[:3,3]
position_joint_3 = T03[:3,3]
position_joint_2 = T02[:3,3]
position_joint_1 = T01[:3,3]

#for animation

x_data ,y_data ,z_data = [] , [] ,[]

values = { Length_link_1:1,Length_link_2:1 ,Length_link_3:1,theta1:0,theta2:0,theta3:0 }

destination = [sy.pi/1 , sy.pi/2 , sy.pi/2 ]
i = 0
for j in range(3):
    i = 0
    while(i < destination[j]):
        if j ==0 :
            values[theta1] = i
        elif j ==1 :
            values[theta2] = i
        else :
            values[theta3] = i
        i += 0.05
        x3 = position_end_effector.subs(values)[0]
        y3 = position_end_effector.subs(values)[1]
        z3 = position_end_effector.subs(values)[2]
        x2 = position_joint_3.subs(values)[0]
        y2 = position_joint_3.subs(values)[1]
        z2 = position_joint_3.subs(values)[2]
        x1 = position_joint_2.subs(values)[0]
        y1 = position_joint_2.subs(values)[1]
        z1 = position_joint_2.subs(values)[2]
        x_data.append([x1,x2,x3])
        y_data.append([y1,y2,y3])
        z_data.append([z1,z2,z3])





from ploting import animation

anim = animation(x_data,y_data,z_data)

# For Live animation 
# anim.plot_3D()
# anim.plotxy()
# anim.plotxz()
# anim.plotyz()

# For saving the Gif

# anim.plot_3D_gif()
# anim.xygif()
# anim.xzgif()
# anim.yzgif()


