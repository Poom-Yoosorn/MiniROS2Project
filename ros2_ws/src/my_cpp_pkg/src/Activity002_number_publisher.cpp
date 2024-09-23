#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"


class Activity002NumberPublisher : public rclcpp::Node 
{
public:
    Activity002NumberPublisher() : Node("Activity002_number_publisher")
    {
        this->declare_parameter("In_number",2);
        this->declare_parameter("In_publish_freq",1.0);

        number_ = this->get_parameter("In_number").as_int();
        publish_frequency_ = this->get_parameter("In_publish_freq").as_double();

        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number",10);
        Timer_ = this->create_wall_timer(std::chrono::milliseconds((int)(1000.0/publish_frequency_)),
                                         std::bind(&Activity002NumberPublisher::publishNumber, this));
        
        RCLCPP_INFO(this->get_logger(), "Activity002_number_publisher has been started");
    }

private:
    void publishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_;
        publisher_->publish(msg);

        RCLCPP_INFO(this->get_logger(), "Activity002_number_publisher has been published");
    }


    int number_;
    double publish_frequency_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr   publisher_;
    rclcpp::TimerBase::SharedPtr Timer_;


};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Activity002NumberPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}