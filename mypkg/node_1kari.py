import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Point
import numpy as np

class Inkinematics():
    def __init__ (self):
        self.node = Node("node_1kari")
        self.sub = self.node.create_subscription(Point,"coordinates",10)
        self.pub = self.node.create_publisher(Float32MultiArray,"velocities",10)
        self.n=0
        
        self.data_n=[0,0]
        self.data_p=[0,0]
        self.delection_n=0
        self.delection_p=0
        self.vc=0
        
        
        
    
    def cal_dil(self,now,past,):
        ret = np.atan2(now[0]-past[0],now[1]-past[1])
        return ret
            
    def cb(self,msg):
        self.data_n.append(msg.x)
        self.data_n.append(msg.y)
        
        self.delection_n = self.cal_dil(self.data_n,(self.data_p))
        
        
        
        
        
        
def main():
    rclpy.init()
    loop=Inkinematics()
    rclpy.spin(Node)