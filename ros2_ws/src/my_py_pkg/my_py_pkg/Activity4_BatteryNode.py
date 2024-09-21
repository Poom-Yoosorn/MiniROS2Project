#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLED
from functools import partial

class BatteryNode(Node): 
    def __init__(self):
        super().__init__("Activity4_BatteryNode") 
        
        self.PercentBattery_ = 100
        self.MemPercentBattery_ = 100
        self.UsingBattery_timer_ = self.create_timer(4.0,self.simulate_UsingBattery)
        self.Mornitortimer_ = self.create_timer(1.0,self.Mornitor)
        
    def call_set_led_server(self, LED_number, state):
        client = self.create_client(SetLED,"set_led")

        while not client.wait_for_service(1.0):
                self.get_logger().warn("Waiting for server set_led...")

        request = SetLED.Request()
        request.lednumber = LED_number
        request.state = state

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_set_led_server, lednumber=LED_number, state=state))
        
    def callback_call_set_led_server(self, future, lednumber, state):
        try:
            response = future.result()
            self.get_logger().info(str(lednumber)+" and ONcmd: "+str(state)+" => "+ str(response.success))
        except Exception as e:
            self.get_logger().error("Service all failed %r" %(e,))
            
    def simulate_UsingBattery(self):
        if self.PercentBattery_ == 100:
            self.PercentBattery_ = 0
            self.call_set_led_server(3,True)
        elif self.PercentBattery_ == 0:
            self.PercentBattery_ = 100
            self.call_set_led_server(3,False)
        
        
            
    def Mornitor(self):
        self.get_logger().info("PercentBattery : " + str(self.PercentBattery_ ))
        self.get_logger().info("MemPercentBattery : " + str(self.MemPercentBattery_ ))
        self.MemPercentBattery_ = self.PercentBattery_ 


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
