cmake_minimum_required(VERSION 3.5)
project(crowdsim)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(
  ${rclcpp_INCLUDE_DIRS}
  ${std_msgs_INCLUDE_DIRS}
)

# Uncomment and define the target if you have the source file
# add_executable(crowdsim_node src/crowdsim_node.cpp)

# Uncomment the following line if you define the target
# ament_target_dependencies(crowdsim_node rclcpp std_msgs)

# Uncomment the following lines if you define the target
# install(TARGETS
#   crowdsim_node
#   DESTINATION lib/${PROJECT_NAME}
# )

ament_package()