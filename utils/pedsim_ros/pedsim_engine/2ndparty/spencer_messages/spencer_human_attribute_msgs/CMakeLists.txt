cmake_minimum_required(VERSION 3.5)
project(spencer_human_attribute_msgs)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}
  ${std_msgs_INCLUDE_DIRS} ${rosidl_default_generators_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES}
  ${std_msgs_LIBRARIES} ${rosidl_default_generators_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES} ${std_msgs_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES})
rosidl_generate_interfaces(${PROJECT_NAME} "msg/CategoricalAttribute.msg"
  "msg/ScalarAttribute.msg" "msg/HumanAttributes.msg"
  DEPENDENCIES builtin_interfaces std_msgs)
################################################
## Declare ROS messages, services and actions ##
################################################

# Generate messages in the 'msg' folder

# Generate services in the 'srv' folder
#add_service_files(
#  FILES
#)

## Generate added messages and services with any dependencies listed here

###################################
## catkin specific configuration ##
###################################

ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_dependencies(std_msgs)
ament_export_dependencies(rosidl_default_generators)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
