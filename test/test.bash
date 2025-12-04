#!/bin/bash
# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

# ROS2 の環境を必ず読み込む
source /opt/ros/humble/setup.bash
source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

grep 'Listen: 10' /tmp/mypkg.log
