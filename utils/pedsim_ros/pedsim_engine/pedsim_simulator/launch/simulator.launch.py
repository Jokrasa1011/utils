import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


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
            name='scene_file',
            default_value=get_package_share_directory(
                'pedsim_simulator') + 'scenarios/social_contexts.xml'
        ),
        launch.actions.DeclareLaunchArgument(
            name='default_queue_size',
            default_value='10'
        ),
        launch.actions.DeclareLaunchArgument(
            name='max_robot_speed',
            default_value='1.5'
        ),
        launch.actions.DeclareLaunchArgument(
            name='robot_mode',
            default_value='1'
        ),
        launch.actions.DeclareLaunchArgument(
            name='enable_groups',
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='with_robot',
            default_value='true'
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
        launch.actions.DeclareLaunchArgument(
            name='simulation_factor',
            default_value='1'
        ),
        launch.actions.DeclareLaunchArgument(
            name='update_rate',
            default_value='25.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='spawn_period',
            default_value='5.0'
        ),
        launch_ros.actions.Node(
            package='pedsim_simulator',
            executable='pedsim_simulator',
            name='pedsim_simulator',
            output='screen',
            parameters=[
                {
                    'scene_file': launch.substitutions.LaunchConfiguration('scene_file')
                },
                {
                    'default_queue_size': launch.substitutions.LaunchConfiguration('default_queue_size')
                },
                {
                    'max_robot_speed': launch.substitutions.LaunchConfiguration('max_robot_speed')
                },
                {
                    'robot_mode': launch.substitutions.LaunchConfiguration('robot_mode')
                },
                {
                    'enable_groups': launch.substitutions.LaunchConfiguration('enable_groups')
                },
                {
                    'simulation_factor': launch.substitutions.LaunchConfiguration('simulation_factor')
                },
                {
                    'update_rate': launch.substitutions.LaunchConfiguration('update_rate')
                },
                {
                    'spawn_period': launch.substitutions.LaunchConfiguration('spawn_period')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
