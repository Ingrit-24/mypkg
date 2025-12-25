# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32MultiArray
import numpy as np

#初期位置＝（０，０）姿勢はｘ軸＋向き
class Calcurate():
    def __init__(self,nh):
        self.pub = nh.create_subscription(Point,"complemented",self.cb,10)
        self.out = nh.create_publisher(Float32MultiArray, "output",10)
        
        self.nh=nh
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
        self.n = 0
        
        self.vx = 0
        self.vy = 0
        self.vc = 0
        
        self.omega = 0
        self.derection1 = 0
        self.derection2 = 0
        
        self.robo_l=150
        self.matrix=np.array([[1/self.robo_l,-1/self.robo_l],[0.5,0.5]])
        
        
    def cb(self,msg):
        self.x1=msg.x
        self.y1=msg.y
        
        if self.n == 0:
            self.n+=1
            return
        
        self.xv = (self.x1-self.x2)/0.5
        self.yv = (self.y1-self.y2)/0.5
        self.cv = np.sqrt(self.xv**2+self.yv**2)
        
        self.derection1=np.arctan2(self.yv,self.xv)
        
        
        if self.derection1 < (-np.pi/2) and (np.pi/2)<self.derection2:
            self.derection2=-2*np.pi+self.derection2
        if self.derection2 < (-np.pi/2) and (np.pi/2)<self.derection1:
            self.derection2=2*np.pi+self.derection2
        
            
        self.omega = (self.derection1-self.derection2)/0.5
        b = np.array([self.omega,self.cv])
        ans = np.linalg.solve(self.matrix, b)
        
        print(str(self.n)+str(ans))
        
        out = Float32MultiArray()
        out.data = [float(self.n*0.5),ans[0],ans[1]]
        self.out.publish(out)
        
        self.x2=self.x1
        self.y2=self.y1
        self.derection2=self.derection1
        self.n+=1
        
        
        
def main():
    rclpy.init()
    node = Node("calcurate")
    calcurate = Calcurate(node)
    rclpy.spin(node)
