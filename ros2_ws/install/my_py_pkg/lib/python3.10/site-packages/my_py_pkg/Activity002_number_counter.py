#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class Activity002NumberCounter(Node): 
    def __init__(self):
        super().__init__("Activity002_number_counter")
        self.Counter_ = 0 
        self.number_count_publisher_ = self.create_publisher(Int64,"number_count", 10)
        self.number_subscriber_ = self.create_subscription(Int64,"number",self.callback_number,10)
        self.reset_count_server_ = self.create_service(SetBool,"reset_counter",self.callback_reset_counter)
        self.get_logger().info("Activity002_number_counter Has Been Started")
        
    def callback_number(self,msg):
        self.Counter_ = self.Counter_+ msg.data
        self.get_logger().info(str(self.Counter_))
        self.publish_number_count(self.Counter_ )
      
    
    def publish_number_count(self,Output):
        new_msg = Int64()
        new_msg.data = Output
        self.number_count_publisher_.publish(new_msg)
        
    def callback_reset_counter(self, request, response):
        if request.data == True:
            self.Counter_ = 0 
            response.success = True
            response.message = 'Reset Done'
        else:
            response.success = False
            response.message = 'Reset NotAgree!!!'
            
        return response
        
        
    

def main(args=None):
    rclpy.init(args=args)
    node = Activity002NumberCounter() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()