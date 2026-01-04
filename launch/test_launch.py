# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    talker = launch_ros.actions.Node(
        package='mypkg',      
        executable='inkinematics',  
        )
    return 0
