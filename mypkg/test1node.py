# Copyright 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Point

class Test(Node):
    def __init__(self):
        super().__init__("test1")
        pub1=Node.create_publisher(Float32,"delta_t",10)
        pub2=Node.create_publisher(Float32,"wheel_dist",10)
        pub3=Node.create_publisher(Point,"coordinates",10)
        self.l=150
        self.dt=0.5
        
        out1=Float32()
        out1.data=self.dt
        out2=Float32()
        out2.data=self.l
        pub1.publish(out1)
        pub2.publish(out2)
        
        Node.create_timer(self.dt,self.cb)
        
    def cb(self):
        rclpy.init()
        node=Test()
        rclpy.spin(node)
        

