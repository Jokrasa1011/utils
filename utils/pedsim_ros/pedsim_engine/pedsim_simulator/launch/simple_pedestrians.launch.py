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
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='visualize',
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='with_robot',
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='simulation_factor',
            default_value='1.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='update_rate',
            default_value='25.0'
        ),
        launch_ros.actions.Node(
            package='rviz',
            executable='rviz',
            name='rviz'
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'pedsim_simulator'), 'launch/simulator.launch.py')
            ),
            launch_arguments={
                'kbd_teleop': launch.substitutions.LaunchConfiguration('kbd_teleop'),
                'rqt_teleop': launch.substitutions.LaunchConfiguration('rqt_teleop'),
                'scene_file': get_package_share_directory('pedsim_simulator') + 'scenarios/social_contexts.xml',
                'with_robot': launch.substitutions.LaunchConfiguration('with_robot'),
                'simulation_factor': launch.substitutions.LaunchConfiguration('simulation_factor'),
                'update_rate': launch.substitutions.LaunchConfiguration('update_rate'),
                'default_queue_size': '10',
                'max_robot_speed': '1.5',
                'robot_mode': '1',
                'enable_groups': 'true',
                'pose_initial_x': '5.0',
                'pose_initial_y': '5.0',
                'pose_initial_theta': '0.7'
            }.items()
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'pedsim_visualizer'), 'launch/visualizer.launch.py')
            )
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
