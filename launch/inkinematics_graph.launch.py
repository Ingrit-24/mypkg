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
    
    inkinematics = launch_ros.actions.Node(
        package='mypkg',      
        executable='inkinematics',  
        parameters=para
        )
    
    graph_v = launch_ros.actions.Node(
        package='mypkg',      
        executable='graph_v', 
        parameters=para
        )
    
    return launch.LaunchDescription([inkinematics,graph_v])   
