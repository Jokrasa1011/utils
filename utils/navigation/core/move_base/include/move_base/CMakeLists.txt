cmake_minimum_required(VERSION 3.5)
project(move_base)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


add_definitions(${EIGEN3_DEFINITIONS})

# dynamic reconfigure
generate_dynamic_reconfigure_options(cfg/MoveBase.cfg)



# move_base
add_library(move_base src/move_base.cpp)
add_dependencies(move_base ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

add_executable(move_base_node src/move_base_node.cpp)
find_package(ament_cmake REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(actionlib REQUIRED)
find_package(rotate_recovery REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(clear_costmap_recovery REQUIRED)
find_package(nav_core REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(navfn REQUIRED)
find_package(base_local_planner REQUIRED)
find_package(rclcpp REQUIRED)
find_package(move_base_msgs REQUIRED)
find_package(cmake_modules REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(pluginlib REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(rclpy REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${Eigen3_INCLUDE_DIRS}
  ${actionlib_INCLUDE_DIRS} ${rotate_recovery_INCLUDE_DIRS}
  ${rosidl_default_generators_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS}
  ${clear_costmap_recovery_INCLUDE_DIRS} ${nav_core_INCLUDE_DIRS}
  ${tf2_ros_INCLUDE_DIRS} ${navfn_INCLUDE_DIRS} ${base_local_planner_INCLUDE_DIRS}
  ${rclcpp_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS} ${move_base_msgs_INCLUDE_DIRS}
  ${cmake_modules_INCLUDE_DIRS} ${tf2_geometry_msgs_INCLUDE_DIRS}
  ${pluginlib_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS} ${std_srvs_INCLUDE_DIRS}
  ${costmap_2d_INCLUDE_DIRS} ${rclpy_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${Eigen3_LIBRARIES}
  ${actionlib_LIBRARIES} ${rotate_recovery_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${clear_costmap_recovery_LIBRARIES} ${nav_core_LIBRARIES} ${tf2_ros_LIBRARIES}
  ${navfn_LIBRARIES} ${base_local_planner_LIBRARIES} ${rclcpp_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${move_base_msgs_LIBRARIES} ${cmake_modules_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${pluginlib_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${std_srvs_LIBRARIES} ${costmap_2d_LIBRARIES} ${rclpy_LIBRARIES})
target_link_libraries(move_base_node ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${Eigen3_LIBRARIES} ${actionlib_LIBRARIES}
  ${rotate_recovery_LIBRARIES} ${rosidl_default_generators_LIBRARIES}
  ${nav_msgs_LIBRARIES} ${clear_costmap_recovery_LIBRARIES} ${nav_core_LIBRARIES}
  ${tf2_ros_LIBRARIES} ${navfn_LIBRARIES} ${base_local_planner_LIBRARIES}
  ${rclcpp_LIBRARIES} ${REQUIRED_LIBRARIES} ${move_base_msgs_LIBRARIES}
  ${cmake_modules_LIBRARIES} ${tf2_geometry_msgs_LIBRARIES} ${pluginlib_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${std_srvs_LIBRARIES} ${costmap_2d_LIBRARIES}
  ${rclpy_LIBRARIES})
add_dependencies(move_base_node ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})
set_target_properties(move_base_node PROPERTIES OUTPUT_NAME move_base)

install(TARGETS move_base_node DESTINATION bin)

install(TARGETS move_base DESTINATION lib)

## Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  FILES_MATCHING
  PATTERN "*.h")

ament_export_dependencies(ament_cmake)
ament_export_dependencies(Eigen3)
ament_export_dependencies(actionlib)
ament_export_dependencies(rotate_recovery)
ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(clear_costmap_recovery)
ament_export_dependencies(nav_core)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(navfn)
ament_export_dependencies(base_local_planner)
ament_export_dependencies(rclcpp)
ament_export_dependencies(move_base_msgs)
ament_export_dependencies(cmake_modules)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(pluginlib)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(std_srvs)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(rclpy)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(move_base ${LIBS})

ament_package()
