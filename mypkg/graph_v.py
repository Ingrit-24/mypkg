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
        
        self.vr=[]
        self.vl=[]
        self.t=[]
        self.n=0
        
        plt.ion() 
        self.fig, self.ax = plt.subplots()
        self.line_r, = self.ax.plot([], [],label="right_verocity")
        self.line_l, = self.ax.plot([], [],label="left_verocity")
        self.ax.legend()
        self.ax.set_xlabel("Time [s]")
        self.ax.set_ylabel("Velocity [mm/s]")
        
    def cb(self,msg):
        self.vr.append(msg.data[0])
        self.vl.append(msg.data[1])
        self.t.append(self.n*self.dt)
        self.n+=1
        
        self.line_r.set_data(self.t, self.vr)
        self.line_l.set_data(self.t, self.vl)
        self.ax.relim()      
        self.ax.autoscale_view()
        plt.draw()      
        plt.pause(0.001)
        
def main():
    rclpy.init()
    node=Graph()
    rclpy.spin(node)
        
        
        
        