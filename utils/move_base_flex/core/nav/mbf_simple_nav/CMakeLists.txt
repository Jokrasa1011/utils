cmake_minimum_required(VERSION 3.5)
project(mbf_simple_nav)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()




set(MBF_SIMPLE_SERVER_LIB mbf_simple_server)
set(MBF_SIMPLE_SERVER_NODE mbf_simple_nav)



add_library(${MBF_SIMPLE_SERVER_LIB} src/simple_navigation_server.cpp)

add_dependencies(${MBF_SIMPLE_SERVER_LIB} ${catkin_EXPORTED_TARGETS})

add_executable(${MBF_SIMPLE_SERVER_NODE} src/simple_server_node.cpp)
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(mbf_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(actionlib_msgs REQUIRED)
find_package(actionlib REQUIRED)
find_package(mbf_abstract_core REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(thread REQUIRED)
find_package(tf2 REQUIRED)
find_package(rclcpp REQUIRED)
find_package(chrono REQUIRED)
find_package(mbf_abstract_nav REQUIRED)
find_package(pluginlib REQUIRED)
find_package(tf2_ros REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${std_msgs_INCLUDE_DIRS}
  ${mbf_msgs_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS} ${std_srvs_INCLUDE_DIRS}
  ${actionlib_msgs_INCLUDE_DIRS} ${actionlib_INCLUDE_DIRS}
  ${mbf_abstract_core_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS}
  ${thread_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS} ${tf2_INCLUDE_DIRS}
  ${rclcpp_INCLUDE_DIRS} ${chrono_INCLUDE_DIRS} ${mbf_abstract_nav_INCLUDE_DIRS}
  ${pluginlib_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${std_msgs_LIBRARIES}
  ${mbf_msgs_LIBRARIES} ${geometry_msgs_LIBRARIES} ${std_srvs_LIBRARIES}
  ${actionlib_msgs_LIBRARIES} ${actionlib_LIBRARIES}
  ${mbf_abstract_core_LIBRARIES} ${nav_msgs_LIBRARIES} ${thread_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${tf2_LIBRARIES} ${rclcpp_LIBRARIES} ${chrono_LIBRARIES}
  ${mbf_abstract_nav_LIBRARIES} ${pluginlib_LIBRARIES} ${tf2_ros_LIBRARIES})
target_link_libraries(${MBF_SIMPLE_SERVER_NODE} ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${std_msgs_LIBRARIES} ${mbf_msgs_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${std_srvs_LIBRARIES} ${actionlib_msgs_LIBRARIES}
  ${actionlib_LIBRARIES} ${mbf_abstract_core_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${thread_LIBRARIES} ${REQUIRED_LIBRARIES} ${tf2_LIBRARIES} ${rclcpp_LIBRARIES}
  ${chrono_LIBRARIES} ${mbf_abstract_nav_LIBRARIES} ${pluginlib_LIBRARIES}
  ${tf2_ros_LIBRARIES})
add_dependencies(${MBF_SIMPLE_SERVER_NODE} ${MBF_SIMPLE_SERVER_LIB})

install(TARGETS ${MBF_SIMPLE_SERVER_LIB} ${MBF_SIMPLE_SERVER_NODE}
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME})


ament_export_dependencies(ament_cmake)
ament_export_dependencies(std_msgs)
ament_export_dependencies(mbf_msgs)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(std_srvs)
ament_export_dependencies(actionlib_msgs)
ament_export_dependencies(actionlib)
ament_export_dependencies(mbf_abstract_core)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(thread)
ament_export_dependencies(tf2)
ament_export_dependencies(rclcpp)
ament_export_dependencies(chrono)
ament_export_dependencies(mbf_abstract_nav)
ament_export_dependencies(pluginlib)
ament_export_dependencies(tf2_ros)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${MBF_SIMPLE_SERVER_LIB} ${LIBS})

ament_package()
