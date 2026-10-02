from launch import LaunchDescription
from launch_ros.actions import Node
import os
from glob import glob


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_mvp',
            executable='robot_simulator',
            name='robot_simulator',
            output='screen'
        ),

        Node(
            package='robot_mvp',
            executable='sensor_node',
            name='sensor_node',
            output='screen'
        ),

        Node(
            package='robot_mvp',
            executable='decision_node',
            name='decision_node',
            output='screen'
        ),
        Node(
           package='robot_mvp',
           executable='visualizer',
           name='visualizer',
           output='screen'
        )
    ])