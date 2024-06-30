import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='range',
            default_value='10.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='resol',
            default_value='360'
        ),
        launch.actions.DeclareLaunchArgument(
            name='origin_x',
            default_value='0.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='origin_y',
            default_value='0.0'
        ),
        launch_ros.actions.Node(
            package='pedsim_sensors',
            executable='pedsim_occlusion_sensor',
            name='pedsim_sensor',
            output='screen',
            parameters=[
                {
                    'pose_initial_x': launch.substitutions.LaunchConfiguration('origin_x')
                },
                {
                    'pose_initial_y': launch.substitutions.LaunchConfiguration('origin_y')
                },
                {
                    'fov_range': launch.substitutions.LaunchConfiguration('range')
                },
                {
                    'rate': '25.0'
                },
                {
                    'resol': launch.substitutions.LaunchConfiguration('resol')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
