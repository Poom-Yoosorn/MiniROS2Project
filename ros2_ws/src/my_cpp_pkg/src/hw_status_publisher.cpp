#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusPublisher : public rclcpp::Node // MODIFY NAME
{
public:
    HardwareStatusPublisher() : Node("hw_status_publisher") // MODIFY NAME
    {
        pub_ = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hardware_status",10);
        timer_ = this->create_wall_timer(   std::chrono::seconds(1),
                                            std::bind(&HardwareStatusPublisher::publishHardwareStatus,this));
        RCLCPP_INFO(this->get_logger(),"Hardware status publisher has been started");

    }

private:
    void publishHardwareStatus()
    {
        auto msg = my_robot_interfaces::msg::HardwareStatus();
        msg.temperature = 57;
        msg.are_motors_ready = false;
        msg.debug_message = "Motor are too hot";

        pub_->publish(msg);

    }

    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
};






int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HardwareStatusPublisher>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}