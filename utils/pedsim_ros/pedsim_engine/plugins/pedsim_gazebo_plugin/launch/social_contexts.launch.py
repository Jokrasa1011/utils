import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='pedsim_gazebo_plugin',
            executable='spawn_pedsim_agents.py',
            name='spawn_pedsim_agents',
            output='screen'
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'gazebo_ros'), 'launch/empty_world.launch.py')
            ),
            launch_arguments={
                'world_name': get_package_share_directory('pedsim_gazebo_plugin') + '/worlds/social_contexts.world'
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
