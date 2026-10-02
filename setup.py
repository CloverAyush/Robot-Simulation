from setuptools import find_packages, setup
import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robot_mvp'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
   data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'launch'),
        glob('launch/*.launch.py')),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ayush',
    maintainer_email='ayush@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_simulator = robot_mvp.robot_sim:main',
            'sensor_node = robot_mvp.sensor_node:main',
            'decision_node = robot_mvp.decision_node:main',
            'visualizer = robot_mvp.visualizer:main',
        ],
    },
)
