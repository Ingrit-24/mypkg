# Copyright 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
import numpy as np

class Odometry(Node):
    def __init__(self):
        super().__init__("odometry")
        self.sub = self.create_subscription(Float32MultiArray,"velocities",self.cb,10)
        self.sub_dt = self.create_subscription(Float32,"delta_t",self.get_dt,1)
        self.sub_l = self.create_subscription(Float32,"wheel_dist",self.get_l,1)
        self.n=0
        self.x=0
        self.y=0
        self.dt=0
        self.l=0
        self.get_sta1=1
        self.get_sta2=1
        self.derection=0
    
    def get_dt (self,msg):
        self.dt=msg.data
        self.get_sta1=1
        self.get_logger().info('odometry get delta_t success')
        
    def get_l (self,msg):
        self.l=msg.data
        self.get_sta2=1
        self.get_logger().info('odometry get wheel_dist success')
    
    def cb(self,msg):
        if self.get_sta1 == 0 or self.get_sta2 == 0:
            return 0
        
        #data[0]が右　  data[1]が左
        self.derection+=(msg.data[0]-msg.data[1])/self.l
        v=(msg.data[0]+msg.data[1])/2
        
        self.x+=np.cos(self.derection)*v*self.dt
        self.y+=np.sin(self.derection)*v*self.dt
        self.get_logger().info(f'{self.x}  {self.y}')

def main():
    rclpy.init()
    node=Odometry()
    rclpy.spin(node) 
        