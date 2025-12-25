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
        executable='calcurate',
        )
    output = launch_ros.actions.Node(
        package='mypkg',
        executable='output',
        output='screen',
        )

    return launch.LaunchDescription([complement, calcurate,output])
