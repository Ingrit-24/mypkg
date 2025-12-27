import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

robot_parameters={
    "wheel_dist": 130, #車輪間距離 [m]
    "dt":0.1,          #制御周期   [s]
    "total_time": 120,  #デモ時間   [s]
}


def generate_launch_description():

    complement = launch_ros.actions.Node(
        package='mypkg',
        executable='complement',
        parameters=[robot_parameters]
        )
    calcurate = launch_ros.actions.Node(
        package='mypkg',
        executable='calculate',
        parameters=[robot_parameters]
        )
    output = launch_ros.actions.Node(
        package='mypkg',
        executable='odometry',
        output='screen',
        parameters=[robot_parameters]
        )

    return launch.LaunchDescription([complement, calcurate,output])
