# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from matplotlib import pyplot as plt

class Graph(Node):
    def __init__(self):
        super().__init__("graph_c")
        self.pub = self.create_subscription(Point,"coordinates_odo",self.cb,10)
        
        self.declare_parameter('delta_t', 0.5)
        self.dt= self.get_parameter('delta_t').get_parameter_value().double_value
        self.get_logger().info(f'graph_c get delta_t success: {self.dt}')
        
        self.x=[0]
        self.y=[0]
        
        plt.ion() 
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [],'b-',label="robot_histry",antialiased=True)
        self.point, = self.ax.plot([], [],"ro")
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.ax.set_xlabel("[mm]")
        self.ax.set_ylabel("[mm]")
        
    def cb(self,msg):
        self.x.append(msg.x)
        self.y.append(msg.y)
        
        self.line.set_data(self.x, self.y)
        self.point.set_data(msg.x,msg.y)
        self.ax.relim()      
        self.ax.autoscale_view()
        plt.draw()      
        plt.pause(0.001)
        
def main():
    rclpy.init()
    node=Graph()
    rclpy.spin(node)
        
        
        
        