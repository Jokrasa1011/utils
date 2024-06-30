import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='map_server',
            executable='map_server',
            name='ms'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
