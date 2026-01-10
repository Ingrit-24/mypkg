# SPDX-FileCopyrightText: 2026 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Point
import numpy as np

class Odometry(Node):
    def __init__(self):
        super().__init__("odometry")
        
        self.declare_parameter('delta_t', 0.5)
        self.declare_parameter('wheel_dist', 150.0)
        
        self.dt= self.get_parameter('delta_t').get_parameter_value().double_value
        self.get_logger().info(f'odometry get delta_t success: {self.dt}')
        
        self.l= self.get_parameter('wheel_dist').get_parameter_value().double_value
        self.get_logger().info(f'odometry get wheel_dist success: {self.l}')
        
        
        self.sub = self.create_subscription(Float32MultiArray,"velocities_odo",self.cb,10)
        self.pub = self.create_publisher(Point,"coordinates_odo",10)
        self.n=0
        self.x=0
        self.y=0
        self.derection=0
    
    def cb(self,msg):

        #data[0]が右　  data[1]が左
        d_theta=(msg.data[0]-msg.data[1])/self.l*self.dt       
        v=(msg.data[0]+msg.data[1])/2
        
        self.x+=np.cos(self.derection+d_theta/2.0)*v*self.dt
        self.y+=np.sin(self.derection+d_theta/2.0)*v*self.dt
        self.get_logger().info(f'X:{self.x:3f}|Y:{self.y:3f}')
        
        
        out = Point()
        out.x=self.x
        out.y=self.y
        self.pub.publish(out)
        self.derection+=d_theta

def main():
    rclpy.init()
    node=Odometry()
    rclpy.spin(node) 
        