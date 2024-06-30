cmake_minimum_required(VERSION 3.5)
project(fake_localization)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()







add_executable(fake_localization fake_localization.cpp)
find_package(ament_cmake REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(angles REQUIRED)
find_package(message_filters REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ros2_console REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(Boost REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(rclpy REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS}
  ${angles_INCLUDE_DIRS} ${message_filters_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS}
  ${rclcpp_INCLUDE_DIRS} ${ros2_console_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS}
  ${tf2_geometry_msgs_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS} ${rclpy_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${angles_LIBRARIES} ${message_filters_LIBRARIES} ${tf2_ros_LIBRARIES}
  ${rclcpp_LIBRARIES} ${ros2_console_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${Boost_LIBRARIES} ${tf2_geometry_msgs_LIBRARIES} ${REQUIRED_LIBRARIES}
  ${rclpy_LIBRARIES})
target_link_libraries(fake_localization ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${nav_msgs_LIBRARIES} ${angles_LIBRARIES}
  ${message_filters_LIBRARIES} ${tf2_ros_LIBRARIES} ${rclcpp_LIBRARIES}
  ${ros2_console_LIBRARIES} ${geometry_msgs_LIBRARIES} ${Boost_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${REQUIRED_LIBRARIES} ${rclpy_LIBRARIES})
add_dependencies(fake_localization ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

install(PROGRAMS static_odom_broadcaster.py
  DESTINATION bin)

install(TARGETS fake_localization DESTINATION bin)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(angles)
ament_export_dependencies(message_filters)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(rclcpp)
ament_export_dependencies(ros2_console)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(Boost)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(rclpy)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
