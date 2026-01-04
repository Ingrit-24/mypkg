#!/bin/bash -xl
# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg test.launch.py > /tmp/mypkg.log


cat /tmp/mypkg.log | grep 'get wheel_dist success'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'get delta_t success'
status=$?  
[ "$status" = "0" ] || exit 1
