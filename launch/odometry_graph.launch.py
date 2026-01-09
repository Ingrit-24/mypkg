# Copyright 2026 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    
    #パラメータ変更はここから
    para=[{
                'delta_t':0.50,
                'wheel_dist':150.0,
            }] 
    
    odometry = launch_ros.actions.Node(
        package='mypkg',      
        executable='odometry',  
        parameters=para
        )
    
    graph_c = launch_ros.actions.Node(
        package='mypkg',      
        executable='graph_c', 
        parameters=para
        )
    
    return launch.LaunchDescription([odometry,graph_c])   