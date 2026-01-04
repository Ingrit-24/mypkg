# Copyright 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
import numpy as np
import time

class Test(Node):
    def __init__(self):
        super().__init__("test1node")
        self.pub1=self.create_publisher(Float32,"delta_t",10)
        self.pub2=self.create_publisher(Float32,"wheel_dist",10)
        self.pub3=self.create_publisher(Point,"coordinates",10)
        self.l=150
        self.dt=0.5
        self.n=0
        
        time.sleep(2.0)
        out1=Float32()
        out1.data=float(self.dt)
        out2=Float32()
        out2.data=float(self.l)
        self.pub1.publish(out1)
        self.pub2.publish(out2)
        
        self.create_timer(self.dt,self.cb)
        
    def cb(self):
        x=np.cos(np.pi*0.05*self.n-np.pi/2)*1000
        y=1000+np.sin(np.pi*0.05*self.n-np.pi/2)*1000
        out=Point()
        out.x=x
        out.y=y
        self.pub3.publish(out)
        self.n+=1
        
        
def main():
    rclpy.init()
    node=Test()
    rclpy.spin(node)
        

