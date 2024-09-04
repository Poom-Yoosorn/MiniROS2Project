#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class RobotNewStationNode(Node):
    def __init__(self):
        super().__init__("robot_new_station") # MODIFY NAME


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewStationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()