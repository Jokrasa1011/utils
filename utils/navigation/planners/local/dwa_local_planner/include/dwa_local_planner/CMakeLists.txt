cmake_minimum_required(VERSION 3.5)
project(dwa_local_planner)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(base_local_planner REQUIRED)
find_package(pluginlib REQUIRED)
find_package(tf2 REQUIRED)
find_package(nav_core REQUIRED)
find_package(cmake_modules REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(angles REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}
  ${Eigen3_INCLUDE_DIRS} ${costmap_2d_INCLUDE_DIRS}
  ${tf2_geometry_msgs_INCLUDE_DIRS} ${base_local_planner_INCLUDE_DIRS}
  ${pluginlib_INCLUDE_DIRS} ${tf2_INCLUDE_DIRS} ${nav_core_INCLUDE_DIRS}
  ${cmake_modules_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS} ${angles_INCLUDE_DIRS}
  ${sensor_msgs_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES}
  ${Eigen3_LIBRARIES} ${costmap_2d_LIBRARIES} ${tf2_geometry_msgs_LIBRARIES}
  ${base_local_planner_LIBRARIES} ${pluginlib_LIBRARIES} ${tf2_LIBRARIES}
  ${nav_core_LIBRARIES} ${cmake_modules_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${angles_LIBRARIES} ${sensor_msgs_LIBRARIES} ${tf2_ros_LIBRARIES}
  ${REQUIRED_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES} ${Eigen3_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${tf2_geometry_msgs_LIBRARIES}
  ${base_local_planner_LIBRARIES} ${pluginlib_LIBRARIES} ${tf2_LIBRARIES}
  ${nav_core_LIBRARIES} ${cmake_modules_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${angles_LIBRARIES} ${sensor_msgs_LIBRARIES} ${tf2_ros_LIBRARIES}
  ${REQUIRED_LIBRARIES})
remove_definitions(-DDISABLE_LIBUSB-1.0)
add_definitions(${EIGEN3_DEFINITIONS})

# dynamic reconfigure
generate_dynamic_reconfigure_options(cfg/DWAPlanner.cfg)


add_library(dwa_local_planner src/dwa_planner.cpp src/dwa_planner_ros.cpp)
add_dependencies(dwa_local_planner ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

install(TARGETS dwa_local_planner
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(FILES blp_plugin.xml DESTINATION share/${PROJECT_NAME})

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  PATTERN ".svn"
  EXCLUDE)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_dependencies(Eigen3)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(base_local_planner)
ament_export_dependencies(pluginlib)
ament_export_dependencies(tf2)
ament_export_dependencies(nav_core)
ament_export_dependencies(cmake_modules)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(angles)
ament_export_dependencies(sensor_msgs)
ament_export_dependencies(tf2_ros)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(dwa_local_planner ${LIBS})

ament_package()
