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
    
    test1 = launch_ros.actions.Node(
        package='mypkg',      
        executable='test1node',  
        )
    
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
    
    return launch.LaunchDescription([inkinematics,test1,graph_v,odometry,graph_c])   
