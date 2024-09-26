from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    
    remap_number_topic = ("number","Poom_number")
    
    number_publisher_node = Node(
        package="my_py_pkg",
        executable="Activity002_number_publisher",
        name="Poom_number_publisher",
        remappings=[
            remap_number_topic
        ],
        parameters=[
            {"In_number":4},
            {"In_publish_freq" : 0.5}
            
        ]
    )
    
    number_counter_node = Node(
        package="my_py_pkg",
        executable="Activity002_number_counter",
        name="Poom_number_counter",
          remappings=[
            remap_number_topic,
            ("number_count","Poom_number_count")
        ]
    )
    
    
    
    
    ld.add_action(number_publisher_node)
    ld.add_action(number_counter_node)
    return ld
