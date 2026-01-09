# Copyright 202 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Point
import numpy as np

class Inkinematics(Node):
    def __init__ (self):
        super().__init__("inkinematics")
        
        self.declare_parameter('delta_t', 0.5)
        self.declare_parameter('wheel_dist', 150.0)
        
        self.dt= self.get_parameter('delta_t').get_parameter_value().double_value
        self.get_logger().info(f'inkinematics get delta_t success: {self.dt}')
        
        self.l= self.get_parameter('wheel_dist').get_parameter_value().double_value
        self.get_logger().info(f'inkinematics get wheel_dist success: {self.l}')
        
        self.sub_coords = self.create_subscription(Point,"coordinates_inkine",self.cb,10)
        self.pub = self.create_publisher(Float32MultiArray,"velocities_inkine",10)
        self.n=0
        
        self.data_n=[0,0]
        self.data_p=[0,0]
        self.derection_n=0
        self.derection_p=0
        self.c=0
        
        self.omega=0
         
   
    def cb(self,msg):
        
        self.data_n[0]=msg.x
        self.data_n[1]=msg.y
        
        self.v = np.sqrt((self.data_n[0]-self.data_p[0])**2+(self.data_n[1]-self.data_p[1])**2)/self.dt
        
        self.derection_n = np.arctan2(self.data_n[1]-self.data_p[1],self.data_n[0]-self.data_p[0])
        
        if self.derection_n < (-np.pi/2) and (np.pi/2)<self.derection_p:
            self.derection_p=-2*np.pi+self.derection_p
        if self.derection_p < (-np.pi/2) and (np.pi/2)<self.derection_n:
            self.derection_p=2*np.pi+self.derection_p
            
        self.omega = (self.derection_n-self.derection_p)/self.dt
        
        matrix=np.array([[1/self.l,-1/self.l],[0.5,0.5]])
        bect = np.array([self.omega,self.v])
        ans = np.linalg.solve(matrix, bect)
        
        #data[0]が右　  data[1]が左
        outputs = Float32MultiArray()
        outputs.data = [float(ans[0]), float(ans[1])]
        self.pub.publish(outputs)
        
        self.get_logger().info(f"VR:{ans[0]:3f}|VL:{ans[1]:3f}")
        
        self.derection_p=self.derection_n
        self.data_p[0]=self.data_n[0]
        self.data_p[1]=self.data_n[1]
        
        
def main():
    rclpy.init()
    node=Inkinematics()
    rclpy.spin(node)