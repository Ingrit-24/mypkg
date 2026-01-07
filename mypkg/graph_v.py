# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from matplotlib import pyplot as plt

class Graph(Node):
    def __init__(self):
        super().__init__("graph_v")
        self.pub = self.create_subscription(Float32MultiArray,"velocities",self.cb,10)
        
        self.declare_parameter('delta_t', 0.5)
        self.dt= self.get_parameter('delta_t').get_parameter_value().double_value
        self.get_logger().info(f'graph_v get delta_t success: {self.dt}')
        
        self.vx=[]
        self.vy=[]
        self.t=[]
        self.n=0
        
    
        
        
    def cb(self,msg):
        self.vx.append(msg.data[0])
        self.vy.append(msg.data[1])
        self.t.append(self.n*self.dt)
        self.n+=0
        
        
        
        