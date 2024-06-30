cmake_minimum_required(VERSION 3.5)
project(mbf_utility)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2 REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(mbf_msgs REQUIRED)
find_package(rclcpp REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS}
  ${tf2_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
  ${tf2_geometry_msgs_INCLUDE_DIRS} ${mbf_msgs_INCLUDE_DIRS}
  ${rclcpp_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${tf2_ros_LIBRARIES} ${tf2_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${tf2_geometry_msgs_LIBRARIES} ${mbf_msgs_LIBRARIES}
  ${rclcpp_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${tf2_ros_LIBRARIES} ${tf2_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${tf2_geometry_msgs_LIBRARIES} ${mbf_msgs_LIBRARIES}
  ${rclcpp_LIBRARIES})


add_library(${PROJECT_NAME} src/navigation_utility.cpp src/robot_information.cpp
  src/odometry_helper.cpp)

add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})


install(TARGETS ${PROJECT_NAME}
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  FILES_MATCHING
  PATTERN "*.h")

ament_export_dependencies(ament_cmake)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(tf2)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(mbf_msgs)
ament_export_dependencies(rclcpp)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${PROJECT_NAME} ${LIBS})

ament_package()
