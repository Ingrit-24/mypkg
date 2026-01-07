# Copyright 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import numpy as np

class Test(Node):
    def __init__(self):
        super().__init__("test2node")
        self.pub=self.create_publisher(Float32MultiArray,"velocities",10)
        self.dt=0.5
        self.n=0
        
        self.create_timer(self.dt,self.cb)
        
    def cb(self):
        right=150
        left=200
        out=Float32MultiArray()
        out.data[0]=right
        out.data[1]=left
        self.pub.publish(out)
        self.n+=1
        
        
def main():
    rclpy.init()
    node=Test()
    rclpy.spin(node)
        

