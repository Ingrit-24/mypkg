# SPDX-FileCopyrightText: 2026 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32MultiArray
import numpy as np

class Test(Node):
    def __init__(self):
        super().__init__("test1node")
        self.pub=self.create_publisher(Point,"coordinates_inkine",10)
        self.pub2=self.create_publisher(Float32MultiArray,"velocities_odo",10)
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
        
        right=200
        left=175
        out2=Float32MultiArray()
        out2.data=[float(right),float(left)]
        self.pub2.publish(out2)
        self.n+=1
        
def main():
    rclpy.init()
    node=Test()
    rclpy.spin(node)
        

