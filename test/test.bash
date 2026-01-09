#!/bin/bash -xl
# SPDX-FileCopyrightText: 2026 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg test.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'inkinematics get delta_t success: 0.25'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'inkinematics get wheel_dist success: 100.0'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'graph_v get delta_t success: 0.25'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'odometry get delta_t success: 0.25'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'odometry get wheel_dist success: 100.0'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'graph_c get delta_t success: 0.25'
status=$?  
[ "$status" = "0" ] || exit 1

cat /tmp/mypkg.log | grep 'VR:'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'VL:'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'X:'
status=$?  
[ "$status" = "0" ] || exit 1
cat /tmp/mypkg.log | grep 'Y:'
status=$?  
[ "$status" = "0" ] || exit 1