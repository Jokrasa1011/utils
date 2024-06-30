cmake_minimum_required(VERSION 3.5)
project(mbf_costmap_nav)

set(CMAKE_CXX_STANDARD 14)



# dynamic reconfigure
generate_dynamic_reconfigure_options(cfg/MoveBaseFlex.cfg)

set(MBF_NAV_CORE_WRAPPER_LIB mbf_nav_core_wrapper)
set(MBF_COSTMAP_2D_SERVER_LIB mbf_costmap_server)
set(MBF_COSTMAP_2D_SERVER_NODE mbf_costmap_nav)



add_library(${MBF_NAV_CORE_WRAPPER_LIB}
  src/nav_core_wrapper/wrapper_global_planner.cpp
  src/nav_core_wrapper/wrapper_local_planner.cpp
  src/nav_core_wrapper/wrapper_recovery_behavior.cpp)
add_dependencies(${MBF_NAV_CORE_WRAPPER_LIB} ${catkin_EXPORTED_TARGETS})

add_library(${MBF_COSTMAP_2D_SERVER_LIB}
  src/mbf_costmap_nav/costmap_navigation_server.cpp
  src/mbf_costmap_nav/costmap_planner_execution.cpp
  src/mbf_costmap_nav/costmap_inter_execution.cpp
  src/mbf_costmap_nav/costmap_controller_execution.cpp
  src/mbf_costmap_nav/costmap_recovery_execution.cpp
  src/mbf_costmap_nav/costmap_wrapper.cpp src/mbf_costmap_nav/footprint_helper.cpp
  src/mbf_costmap_nav/free_pose_search.cpp
  src/mbf_costmap_nav/free_pose_search_viz.cpp)
add_dependencies(${MBF_COSTMAP_2D_SERVER_LIB} ${catkin_EXPORTED_TARGETS})
add_dependencies(${MBF_COSTMAP_2D_SERVER_LIB} ${MBF_NAV_CORE_WRAPPER_LIB})
add_dependencies(${MBF_COSTMAP_2D_SERVER_LIB} ${PROJECT_NAME}_gencfg)


add_executable(${MBF_COSTMAP_2D_SERVER_NODE} src/move_base_server_node.cpp)
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(mbf_abstract_nav REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(chrono REQUIRED)
find_package(thread REQUIRED)
find_package(map_server REQUIRED)
find_package(angles REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(mbf_costmap_core REQUIRED)
find_package(std_srvs REQUIRED)
find_package(tf2 REQUIRED)
find_package(rostest REQUIRED)
find_package(mbf_msgs REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(mbf_utility REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_core REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${std_msgs_INCLUDE_DIRS}
  ${mbf_abstract_nav_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS} ${chrono_INCLUDE_DIRS}
  ${thread_INCLUDE_DIRS} ${map_server_INCLUDE_DIRS} ${angles_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS} ${mbf_costmap_core_INCLUDE_DIRS}
  ${std_srvs_INCLUDE_DIRS} ${tf2_INCLUDE_DIRS} ${rostest_INCLUDE_DIRS}
  ${mbf_msgs_INCLUDE_DIRS} ${costmap_2d_INCLUDE_DIRS} ${mbf_utility_INCLUDE_DIRS}
  ${rclcpp_INCLUDE_DIRS} ${nav_core_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${std_msgs_LIBRARIES}
  ${mbf_abstract_nav_LIBRARIES} ${nav_msgs_LIBRARIES} ${chrono_LIBRARIES}
  ${thread_LIBRARIES} ${map_server_LIBRARIES} ${angles_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${mbf_costmap_core_LIBRARIES} ${std_srvs_LIBRARIES}
  ${tf2_LIBRARIES} ${rostest_LIBRARIES} ${mbf_msgs_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${mbf_utility_LIBRARIES} ${rclcpp_LIBRARIES}
  ${nav_core_LIBRARIES} ${REQUIRED_LIBRARIES})
target_link_libraries(${MBF_COSTMAP_2D_SERVER_NODE} ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${std_msgs_LIBRARIES}
  ${mbf_abstract_nav_LIBRARIES} ${nav_msgs_LIBRARIES} ${chrono_LIBRARIES}
  ${thread_LIBRARIES} ${map_server_LIBRARIES} ${angles_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${mbf_costmap_core_LIBRARIES} ${std_srvs_LIBRARIES}
  ${tf2_LIBRARIES} ${rostest_LIBRARIES} ${mbf_msgs_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${mbf_utility_LIBRARIES} ${rclcpp_LIBRARIES}
  ${nav_core_LIBRARIES} ${REQUIRED_LIBRARIES})
add_dependencies(${MBF_COSTMAP_2D_SERVER_NODE} ${MBF_COSTMAP_2D_SERVER_LIB})

install(TARGETS ${MBF_NAV_CORE_WRAPPER_LIB} ${MBF_COSTMAP_2D_SERVER_LIB}
  ${MBF_COSTMAP_2D_SERVER_NODE}
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME})

install(PROGRAMS scripts/move_base_legacy_relay.py
  DESTINATION bin)

#############
## Test    ##
#############

if(CATKIN_ENABLE_TESTING)

  add_rostest_gtest(free_pose_search_test test/free_pose_search.test
    test/free_pose_search_test.cpp)
endif()

ament_export_dependencies(ament_cmake)
ament_export_dependencies(std_msgs)
ament_export_dependencies(mbf_abstract_nav)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(chrono)
ament_export_dependencies(thread)
ament_export_dependencies(map_server)
ament_export_dependencies(angles)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(mbf_costmap_core)
ament_export_dependencies(std_srvs)
ament_export_dependencies(tf2)
ament_export_dependencies(rostest)
ament_export_dependencies(mbf_msgs)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(mbf_utility)
ament_export_dependencies(rclcpp)
ament_export_dependencies(nav_core)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${MBF_NAV_CORE_WRAPPER_LIB} ${MBF_COSTMAP_2D_SERVER_LIB}
  ${LIBS})

ament_package()
