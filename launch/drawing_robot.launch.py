import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    complement = launch_ros.actions.Node(
        package='mypkg',
        executable='complement',
        )
    calcurate = launch_ros.actions.Node(
        package='mypkg',
        executable='calculate',
        )
    output = launch_ros.actions.Node(
        package='mypkg',
        executable='odometry',
        output='screen',
        )

    return launch.LaunchDescription([complement, calcurate,output])
