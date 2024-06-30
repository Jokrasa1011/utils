import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='amcl',
            executable='amcl',
            name='amcl',
            parameters=[
                {
                    'odom_model_type': 'omni'
                },
                {
                    'odom_alpha5': '0.1'
                },
                {
                    'gui_publish_rate': '10.0'
                },
                {
                    'laser_max_beams': '30'
                },
                {
                    'min_particles': '500'
                },
                {
                    'max_particles': '5000'
                },
                {
                    'kld_err': '0.05'
                },
                {
                    'kld_z': '0.99'
                },
                {
                    'odom_alpha1': '0.2'
                },
                {
                    'odom_alpha2': '0.2'
                },
                {
                    'odom_alpha3': '0.8'
                },
                {
                    'odom_alpha4': '0.2'
                },
                {
                    'laser_z_hit': '0.5'
                },
                {
                    'laser_z_short': '0.05'
                },
                {
                    'laser_z_max': '0.05'
                },
                {
                    'laser_z_rand': '0.5'
                },
                {
                    'laser_sigma_hit': '0.2'
                },
                {
                    'laser_lambda_short': '0.1'
                },
                {
                    'laser_model_type': 'likelihood_field'
                },
                {
                    'laser_likelihood_max_dist': '2.0'
                },
                {
                    'update_min_d': '0.2'
                },
                {
                    'update_min_a': '0.5'
                },
                {
                    'odom_frame_id': 'odom'
                },
                {
                    'resample_interval': '1'
                },
                {
                    'transform_tolerance': '0.1'
                },
                {
                    'recovery_alpha_slow': '0.0'
                },
                {
                    'recovery_alpha_fast': '0.0'
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
