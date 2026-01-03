# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import csv
import numpy as np
from scipy.interpolate import make_interp_spline
import os
from ament_index_python.packages import get_package_share_directory


class Complrment(Node):
    def __init__(self,nh):
        super().__init__('complement')
        self.pub = nh.create_publisher(Point, "complemented",10)
        self.declare_parameter('dt', 0.5)
        self.dt = self.get_parameter('dt').value
        self.declare_parameter('total_time', 50)
        self.total_time = self.get_parameter('total_time').value
        
        self.n = 0
        self.data_x=[]
        self.data_y=[]
        
        package_dir = get_package_share_directory('mypkg')
        csv_path = os.path.join(package_dir,'data', 'coordinatesdata.csv')
        with open(csv_path,"r",encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                self.data_x.append(float(row[0]))
                self.data_y.append(float(row[1]))
                
        self.data_dt=float(self.total_time)/len(self.data_x)
        self.data_t=[]
        for i in range(len(self.data_x)):
            self.data_t.append(self.data_dt*i)

        self.x_np = np.array(self.data_x)
        self.y_np = np.array(self.data_y)
        self.t_np = np.array(self.data_t)

        self.points = np.vstack((self.x_np,self.y_np)).T
        self.sp_points = make_interp_spline(self.t_np, self.points, k=3)
        
        self.timer=nh.create_timer(self.dt, self.cb)

    def cb(self):
        if self.n*self.dt > self.t_np[-1]:
            self.timer.cancel()

        msg = Point()
        msg.x = float(self.sp_points(self.n*self.dt)[0])
        msg.y = float(self.sp_points(self.n*self.dt)[1])
        msg.z = 0.0
        self.pub.publish(msg)
        self.n += 1


def main():
    rclpy.init()
    node = Node("complementer")
    complremented = Complrment(node)
    rclpy.spin(node)
