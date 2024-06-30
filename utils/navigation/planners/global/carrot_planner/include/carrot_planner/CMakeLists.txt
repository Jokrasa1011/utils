cmake_minimum_required(VERSION 3.5)
project(carrot_planner)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(base_local_planner REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(angles REQUIRED)
find_package(nav_core REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${base_local_planner_INCLUDE_DIRS}
  ${tf2_geometry_msgs_INCLUDE_DIRS} ${costmap_2d_INCLUDE_DIRS}
  ${pluginlib_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS} ${tf2_INCLUDE_DIRS}
  ${tf2_ros_INCLUDE_DIRS} ${angles_INCLUDE_DIRS} ${nav_core_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${base_local_planner_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${costmap_2d_LIBRARIES} ${pluginlib_LIBRARIES}
  ${rclcpp_LIBRARIES} ${tf2_LIBRARIES} ${tf2_ros_LIBRARIES} ${angles_LIBRARIES}
  ${nav_core_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${base_local_planner_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${costmap_2d_LIBRARIES} ${pluginlib_LIBRARIES}
  ${rclcpp_LIBRARIES} ${tf2_LIBRARIES} ${tf2_ros_LIBRARIES} ${angles_LIBRARIES}
  ${nav_core_LIBRARIES})
add_definitions(${EIGEN3_DEFINITIONS})


add_library(carrot_planner src/carrot_planner.cpp)
add_dependencies(carrot_planner ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

install(TARGETS carrot_planner
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  PATTERN ".svn"
  EXCLUDE)

install(FILES bgp_plugin.xml DESTINATION share/${PROJECT_NAME})



ament_export_dependencies(ament_cmake)
ament_export_dependencies(base_local_planner)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(pluginlib)
ament_export_dependencies(rclcpp)
ament_export_dependencies(tf2)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(angles)
ament_export_dependencies(nav_core)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(carrot_planner ${LIBS})

ament_package()
