#!/bin/bash -xl
# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 11 ros2 launch mypkg drowing_robot.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'time:9.0'
