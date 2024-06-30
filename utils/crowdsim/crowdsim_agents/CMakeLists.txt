cmake_minimum_required(VERSION 3.5)
project(crowdsim_agents)

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

add_executable(crowdsim_agents_node src/crowdsim_agents_node.cpp)

ament_target_dependencies(crowdsim_agents_node
  rclcpp
  std_msgs
)

install(TARGETS
  crowdsim_agents_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()