from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    robot_names = ["Poom","Mo","yoyo","Robert","R2D2"]
    robot_new_station_nodes = []
    
    
    for name in robot_names:
        robot_new_station_nodes.append(Node(
          package="my_cpp_pkg",
          executable="robot_news_station",
          name="robot_news_station_"+name.lower(),
          parameters=[{"robot_name":name}]
        ))
        
    smartphone_Node = Node(
        package="my_cpp_pkg",
        executable="smartphone"
    )
    
    for node in robot_new_station_nodes:
        ld.add_action(node)
    
    ld.add_action(smartphone_Node)
    return ld