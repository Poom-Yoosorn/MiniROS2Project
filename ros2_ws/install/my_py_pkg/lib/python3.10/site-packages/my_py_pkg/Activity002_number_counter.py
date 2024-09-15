#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class Activity002NumberCounter(Node): 
    def __init__(self):
        super().__init__("Activity002_number_counter")
        self.Counter_ = 0 
        self.publisher_ = self.create_publisher(Int64,"number_count", 10)
        self.subscriber_ = self.create_subscription(Int64,"number",self.callback_number_count,10)
        self.get_logger().info("Activity002_number_counter Has Been Started")
        
    def callback_number_count(self,msg):
        self.Counter_ = self.Counter_+ msg.data
        self.get_logger().info(str(self.Counter_))
        self.publish_number_Counter()
      
    
    def publish_number_Counter(self):
        #publish number_Counter
        new_msg = Int64()
        new_msg.data = self.Counter_
        self.publisher_.publish(new_msg)
        #publish number_Counter
    

def main(args=None):
    rclpy.init(args=args)
    node = Activity002NumberCounter() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()