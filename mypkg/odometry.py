# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import numpy as np
import matplotlib.pyplot as plt

class OdometryPlotter(Node):
    def __init__(self):
        super().__init__('odometry')
        self.sub = self.create_subscription(Float32MultiArray, "output", self.cb,10)
        
        self.declare_parameter('dt', 0.5)
        self.dt = self.get_parameter('dt').value
        self.declare_parameter('wheel_dist', 150)
        self.robo_l = self.get_parameter('wheel_dist').value
        
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0     

        self.history_x = [0.0]
        self.history_y = [0.0]

        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.line, = self.ax.plot([], [], 'b-', label='Estimated Path')
        self.robot_pos, = self.ax.plot([], [], 'ro', label='Robot') 
        
        self.ax.set_title("Drowing_Robot_Orbit")
        self.ax.set_xlabel("X [mm]")
        self.ax.set_ylabel("Y [mm]")
        self.ax.set_xlim(-1000, 1000)
        self.ax.set_ylim(-1000, 1000)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.ax.legend()

    def cb(self, msg):
        t, vr, vl = msg.data
        self.get_logger().info(f"|Time:{msg.data[0]:>8.2f}|VR:{msg.data[1]:>8.2f}|VL:{msg.data[2]:>8.2f}|")
        
        v = (vr + vl) / 2.0
        omega = (vr - vl) / self.robo_l
        
        self.x += v * np.cos(self.theta) * self.dt
        self.y += v * np.sin(self.theta) * self.dt
        self.theta += omega * self.dt
        
        self.history_x.append(self.x)
        self.history_y.append(self.y)
        
        if   max(self.history_x) > 900:
            if min(self.history_x) < -900:
                self.ax.set_xlim(min(self.history_x) - 100, max(self.history_x) + 100)
            else:  
                self.ax.set_xlim( -1000, max(self.history_x) + 100)
            
        elif min(self.history_x) < -900:
            self.ax.set_xlim(min(self.history_x) - 100 , 1000)
            
            
        if   max(self.history_y) > 900:
            if min(self.history_y) < -900:
                self.ax.set_ylim(min(self.history_y) - 100, max(self.history_y) + 100)
            else:    
                self.ax.set_ylim( -1000, max(self.history_y) + 100)
            
        elif min(self.history_y) < -900:
            self.ax.set_ylim(min(self.history_y) - 100 , 1000)
            
            
        self.line.set_data(self.history_x, self.history_y)
        self.robot_pos.set_data([self.x], [self.y]) 
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

        
            
def main():
    rclpy.init()
    node = OdometryPlotter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        plt.ioff()
        plt.show() 
        node.destroy_node()
        rclpy.shutdown()

