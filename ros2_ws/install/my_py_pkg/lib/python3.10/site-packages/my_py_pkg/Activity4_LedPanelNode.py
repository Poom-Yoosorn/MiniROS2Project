#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLED
from my_robot_interfaces.msg import LedStatus

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("Activity4_LedPanelNode")
        self.server_ = self.create_service(SetLED,"set_led",self.callback_set_led)
        self.led_status_publisher_ = self.create_publisher(LedStatus,"led_status",10)
        self.timer_ = self.create_timer(1.0,self.publish_led_status)
        self.LED3 = False
        self.get_logger().info("LedPanel Server has been started")
        
    def callback_set_led(self, request, response):
        
        if request.lednumber == 3 and request.state == True:
            self.LED3 = True
            response.success = True
        elif request.lednumber == 3 and request.state == False:
            self.LED3 = False
            response.success = False
        
        self.get_logger().info("LED3: " + str(self.LED3))
        return response
    
    def publish_led_status(self):
        msg = LedStatus()
        msg.led3_on = self.LED3
        self.led_status_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()