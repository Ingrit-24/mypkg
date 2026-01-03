import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
import numpy as np

class Inkinematics():
    def __init__ (self):
        self.node = Node("node_1kari")
        self.sub_dt = self.node.create_subscription(Float32,"delta_t",self.get_dt,1)
        self.sub_dt = self.node.create_subscription(Float32,"wheel_dist",self.get_l,1)
        self.sub_coords = self.node.create_subscription(Point,"coordinates",10)
        self.pub = self.node.create_publisher(Float32MultiArray,"velocities",10)
        self.n=0
        
        self.data_n=[0,0]
        self.data_p=[0,0]
        self.delection_n=0
        self.delection_p=0
        self.vc=0
        
        self.dt
        self.l
        self.get_sta1=0
        self.get_sta2=0
        
        self.matrix=np.array([[1/self.l,-1/self.l],[0.5,0.5]])
        self.omega=0
         
    def get_dt (self,msg):
        self.dt=msg.data
        self.get_sta1=1
        
    def get_dt (self,msg):
        self.l=msg.data
        self.get_sta2=1
            
    def cb(self,msg):
        if self.get_sta1 == 0 or self.get_sta2 == 0:
            return 0
        
        self.data_n.append(msg.x)
        self.data_n.append(msg.y)
        
        self.delection_n = np.atan2(self.data_n[0]-self.data_p[0],self.data_n[1]-self.data_p[1])
        
        self.omega = (self.delection_n-self.delection_p)/self.dt
        
        
        
def main():
    rclpy.init()
    loop=Inkinematics()
    rclpy.spin(Node)