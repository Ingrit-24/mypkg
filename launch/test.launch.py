# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    
    test1 = launch_ros.actions.Node(
        package='mypkg',      
        executable='test1node',  
        )
    
    inkinematics = launch_ros.actions.Node(
        package='mypkg',      
        executable='inkinematics',  
        parameters=[{
                'delta_t':0.25,
                'wheel_dist':100.0,
            }]
        )
    odometry = launch_ros.actions.Node(
        package='mypkg',      
        executable='odometry', 
        parameters=[{
                'delta_t':0.25,
                'wheel_dist':100.0,
            }] 
        )
    
    return launch.LaunchDescription([inkinematics,odometry,test1])   
