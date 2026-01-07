# Copyright 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import numpy as np

class Test(Node):
    def __init__(self):
        super().__init__("test1node")
        self.pub=self.create_publisher(Point,"coordinates",10)
        self.l=150
        self.dt=0.5
        self.n=0
        
        self.create_timer(self.dt,self.cb)
        
    def cb(self):
        x=self.n*50.0
        y=1000+np.sin(np.pi*0.025*self.n-np.pi/2)*1000
        out=Point()
        out.x=x
        out.y=y
        self.pub.publish(out)
        self.n+=1
        
        
def main():
    rclpy.init()
    node=Test()
    rclpy.spin(node)
        

