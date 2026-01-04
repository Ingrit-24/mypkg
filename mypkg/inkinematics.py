# Copyright 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
import numpy as np

class Inkinematics(Node):
    def __init__ (self):
        super().__init__("inkinematics")
        self.sub_dt = self.create_subscription(Float32,"delta_t",self.get_dt,1)
        self.sub_l = self.create_subscription(Float32,"wheel_dist",self.get_l,1)
        self.sub_coords = self.create_subscription(Point,"coordinates",self.cb,10)
        self.pub = self.create_publisher(Float32MultiArray,"velocities",10)
        self.n=0
        
        self.data_n=[0,0]
        self.data_p=[0,0]
        self.derection_n=0
        self.derection_p=0
        self.c=0
        
        self.dt=0
        self.l=0
        self.get_sta1=0
        self.get_sta2=0
        
        self.omega=0
         
    def get_dt (self,msg):
        self.dt=msg.data
        self.get_sta1=1
        self.get_logger().info('get delta_t success')
        
    def get_l (self,msg):
        self.l=msg.data
        self.get_sta2=1
        self.get_logger().info('get wheel_dist success')
            
    def cb(self,msg):
        if self.get_sta1 == 0 or self.get_sta2 == 0:
            return 0
        
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
        
        outputs = Float32MultiArray()
        outputs.data = [float(ans[0]), float(ans[1])]
        self.pub.publish(outputs)
        self.get_logger().info(f"{ans[0]}+{str(ans[1])}")
        
        self.derection_p=self.derection_n
        self.data_p[0]=self.data_n[0]
        self.data_p[1]=self.data_n[1]
        
        
def main():
    rclpy.init()
    node=Inkinematics()
    rclpy.spin(node)