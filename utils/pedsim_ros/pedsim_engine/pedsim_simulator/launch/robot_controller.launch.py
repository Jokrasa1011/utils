import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='kbd_teleop',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='rqt_teleop',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='pose_initial_x',
            default_value='5.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='pose_initial_y',
            default_value='5.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='pose_initial_theta',
            default_value='0.0'
        ),
        launch_ros.actions.Node(
            package='pedsim_simulator',
            executable='simulate_diff_drive_robot',
            name='driving_controller',
            output='screen',
            parameters=[
                {
                    'pose_initial_x': launch.substitutions.LaunchConfiguration('pose_initial_x')
                },
                {
                    'pose_initial_y': launch.substitutions.LaunchConfiguration('pose_initial_y')
                },
                {
                    'pose_initial_theta': launch.substitutions.LaunchConfiguration('pose_initial_theta')
                }
            ]
        ),
        launch_ros.actions.Node(
            package='pedsim_simulator',
            executable='keyboard_teleop.py',
            name='pedsim_keyboard_teleop',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='rqt_robot_steering',
            executable='rqt_robot_steering',
            name='rqt_robot_steering'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
