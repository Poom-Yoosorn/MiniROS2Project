#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"


class RobotNewStationNode : public rclcpp::Node 
{
public:
    RobotNewStationNode() : Node("robot_news_station"), robot_name_("R2D2")
    {
        this->declare_parameter("robot_name","R2D2");
        robot_name_ = this->get_parameter("robot_name").as_string();

        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news",10);
        Timer_ = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&RobotNewStationNode::publishNews, this));

        RCLCPP_INFO(this->get_logger(), "Robot New Station CPP has been started");
    }

private:
    void publishNews()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = std::string("Hi,This is ")+robot_name_+std::string(" from the robot new station");
        publisher_->publish(msg);

        RCLCPP_INFO(this->get_logger(), "Robot New Station has been published");
    }


    std::string robot_name_;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr   publisher_;
    rclcpp::TimerBase::SharedPtr Timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewStationNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}