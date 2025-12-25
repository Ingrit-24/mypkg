import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import numpy as np
import matplotlib.pyplot as plt

class OdometryPlotter(Node):
    def __init__(self):
        super().__init__('odometory')
        self.sub = self.create_subscription(Float32MultiArray, "output", self.cb,10)
        
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        
        self.robo_l = 150.0  
        self.dt = 0.5        

        self.history_x = [0.0]
        self.history_y = [0.0]

        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.line, = self.ax.plot([], [], 'b-', label='Estimated Path')
        self.robot_pos, = self.ax.plot([], [], 'ro', label='Robot') 
        
        self.ax.set_title("Drowing_Robot_Orbit")
        self.ax.set_xlabel("X [mm]")
        self.ax.set_ylabel("Y [mm]")
        self.ax.set_xlim(-1200, 1200)
        self.ax.set_ylim(-200, 3200)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.ax.legend()

    def cb(self, msg):
        t, vr, vl = msg.data
        self.get_logger().info(f"time:{msg.data[0]} VR:{msg.data[1]} VL:{msg.data[2]}")
        
        v = (vr + vl) / 2.0
        omega = (vr - vl) / self.robo_l
        
        self.x += v * np.cos(self.theta) * self.dt
        self.y += v * np.sin(self.theta) * self.dt
        self.theta += omega * self.dt
        
        self.history_x.append(self.x)
        self.history_y.append(self.y)
        
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

