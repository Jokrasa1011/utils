import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='costmap_2d',
            executable='costmap_2d_markers',
            name='voxel_visualizer',
            parameters=[
                {
                    '/use_sim_time': 'true'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='costmap_2d',
            executable='costmap_2d_node',
            name='costmap_node',
            parameters=[
                {
                    '/use_sim_time': 'true'
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
