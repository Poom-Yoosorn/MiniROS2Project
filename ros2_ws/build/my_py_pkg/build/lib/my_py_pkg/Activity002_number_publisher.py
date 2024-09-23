#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("Activity002_number_publisher") # MODIFY NAME

        self.declare_parameter("In_number", 2)
        self.declare_parameter("In_publish_freq",1.0)
        
        self.number_ = self.get_parameter("In_number").value
        self.publish_frequency_ = self.get_parameter("In_publish_freq").value
        
        self.number_publisher_ = self.create_publisher(Int64, "number", 10)
        self.number_timer_ = self.create_timer(1.0 / self.publish_frequency_, self.publish_number)
        self.get_logger().info("Number Pub has been started")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_ 
        self.number_publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()