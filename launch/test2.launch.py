# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    
    para=[{
                'delta_t':0.25,
                'wheel_dist':100.0,
            }] 
    
    test2 = launch_ros.actions.Node(
        package='mypkg',      
        executable='test2node',  
        )
    
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
    
    return launch.LaunchDescription([test2,odometry,graph_c])   
