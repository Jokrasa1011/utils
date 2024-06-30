import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='world_path',
            default_value=get_package_share_directory(
                'flatland_server') + '/test/conestogo_office_test/world.yaml'
        ),
        launch.actions.DeclareLaunchArgument(
            name='update_rate',
            default_value='200.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='step_size',
            default_value='0.1'
        ),
        launch.actions.DeclareLaunchArgument(
            name='show_viz',
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='viz_pub_rate',
            default_value='30.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='use_rviz',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='flatland_viz',
            executable='flatland_viz',
            name='flatland_viz',
            output='screen',
            on_exit=launch.actions.Shutdown(),
            parameters=[
                {
                    'use_sim_time': 'true'
                }
            ],
            condition=launch.conditions.IfCondition(
                launch.substitutions.LaunchConfiguration('show_viz'))
        ),
        launch_ros.actions.Node(
            package='flatland_server',
            executable='flatland_server',
            name='flatland_server',
            output='screen',
            parameters=[
                {
                    'use_sim_time': 'true'
                },
                {
                    'world_path': launch.substitutions.LaunchConfiguration('world_path')
                },
                {
                    'update_rate': launch.substitutions.LaunchConfiguration('update_rate')
                },
                {
                    'step_size': launch.substitutions.LaunchConfiguration('step_size')
                },
                {
                    'show_viz': launch.substitutions.LaunchConfiguration('show_viz')
                },
                {
                    'viz_pub_rate': launch.substitutions.LaunchConfiguration('viz_pub_rate')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
