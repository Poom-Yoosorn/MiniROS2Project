#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLedOriginal
from functools import partial

class BatteryNode(Node): 
    def __init__(self):
        super().__init__("battery") 
        self.battery_state_ = "full"
        self.last_time_battery_state_changed_ = self.get_current_time_secounds()
        self.battery_timer_ = self.create_timer(0.1, self.check_battery_state)
        self.get_logger().info("BatteryNode has been started.....At time : " + str(self.get_current_time_secounds()))

    def get_current_time_secounds(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 1000000000.0
        
        
    def check_battery_state(self):
        time_now = self.get_current_time_secounds()
        if self.battery_state_ == "full":
            if time_now - self.last_time_battery_state_changed_ > 4.0 :
                self.battery_state_ = "empty"
                self.get_logger().info("Battery is empty! changing Battery..... At time :" + str(time_now) + self.battery_state_)
                self.last_time_battery_state_changed_ = time_now
                self.call_set_led_server(3, 1)
        
        else:
            if time_now - self.last_time_battery_state_changed_ > 6.0 :
                self.battery_state_ = "full"
                self.get_logger().info("Battery is Full! Using Battery..... At time :"+ str(time_now) + self.battery_state_)
                self.last_time_battery_state_changed_ = time_now
                self.call_set_led_server(3, 0)


    def call_set_led_server(self, led_number, state):
        client = self.create_client(SetLedOriginal,"set_led")
    
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for set_led_server...")
    
        request = SetLedOriginal.Request()
        request.led_number = led_number
        request.state = state
        
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_set_led_server, led_number=led_number, state=state))
    
    
    def callback_call_set_led_server(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info("SetLED : " + str(response.success))
            
        except Exception as e:
            self.get_logger().error("Service all failed %r" %(e,))






def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()