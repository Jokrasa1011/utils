import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='scene_file',
            default_value=''
        ),
        launch.actions.DeclareLaunchArgument(
            name='visualize',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='pedsim_simulator',
            executable='pedsim_simulator',
            name='pedsim_simulator',
            on_exit=launch.actions.Shutdown(),
            parameters=[
                {
                    'simulation_factor': '1'
                },
                {
                    'pedsim_update_rate': '30.0'
                },
                {
                    'scene_file': launch.substitutions.LaunchConfiguration('scene_file')
                }
            ]
        ),
        launch_ros.actions.Node(
            package='pedsim_visualizer',
            executable='pedsim_visualizer_node',
            name='pedsim_visualizer'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
