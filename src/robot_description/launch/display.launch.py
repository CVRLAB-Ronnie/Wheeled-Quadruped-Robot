
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    pkg_share = get_package_share_directory("robot_description")

    xacro_file = os.path.join(
        pkg_share,
        "urdf",
        "pupper",
        "pupper.urdf.xacro"
    )

    rviz_file = os.path.join(
        pkg_share,
        "config",
        "display.rviz"
    )

    robot_description = {
        "robot_description": Command([
            "xacro ",
            xacro_file
        ])
    }

    use_gui = LaunchConfiguration("gui")

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[robot_description]
    )

    joint_state_publisher = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output="screen",
        condition=None
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_file]
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz2
    ])

