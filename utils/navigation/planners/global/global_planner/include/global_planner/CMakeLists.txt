cmake_minimum_required(VERSION 3.5)
project(global_planner)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



generate_dynamic_reconfigure_options(cfg/GlobalPlanner.cfg)



add_library(${PROJECT_NAME} src/quadratic_calculator.cpp src/dijkstra.cpp
  src/astar.cpp src/grid_path.cpp src/gradient_path.cpp src/orientation_filter.cpp
  src/planner_core.cpp)
add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

add_executable(planner src/plan_node.cpp)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(pluginlib REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(angles REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(nav_core REQUIRED)
find_package(navfn REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}
  ${tf2_geometry_msgs_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS}
  ${pluginlib_INCLUDE_DIRS} ${costmap_2d_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS} ${angles_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS}
  ${nav_core_INCLUDE_DIRS} ${navfn_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${tf2_ros_LIBRARIES} ${pluginlib_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${geometry_msgs_LIBRARIES} ${angles_LIBRARIES}
  ${nav_msgs_LIBRARIES} ${nav_core_LIBRARIES} ${navfn_LIBRARIES})
target_link_libraries(planner ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${tf2_ros_LIBRARIES} ${pluginlib_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${geometry_msgs_LIBRARIES} ${angles_LIBRARIES}
  ${nav_msgs_LIBRARIES} ${nav_core_LIBRARIES} ${navfn_LIBRARIES})
add_dependencies(planner ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

install(TARGETS ${PROJECT_NAME}
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(TARGETS planner RUNTIME DESTINATION bin)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  PATTERN ".svn"
  EXCLUDE)

install(FILES bgp_plugin.xml DESTINATION share/${PROJECT_NAME})

ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(pluginlib)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(angles)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(nav_core)
ament_export_dependencies(navfn)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${PROJECT_NAME} ${LIBS})

ament_package()
