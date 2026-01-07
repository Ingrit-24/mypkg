# SPDX-FileCopyrightText: 2025 Shogo Takizawa
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name,'data'), glob('data/*.csv')),
    ],
    install_requires=['setuptools','numpy'],
    zip_safe=True,
    maintainer='Shogo Takizawa',
    maintainer_email='shogo.taki.2402@icloud.com',
    description='ロボットシステム学',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'inkinematics = mypkg.inkinematics:main',
            'test1node = mypkg.test1node:main',
            'odometry = mypkg.odometry:main',
            'graph_v = mypkg.graph_v:main',
        ],
    },
)
