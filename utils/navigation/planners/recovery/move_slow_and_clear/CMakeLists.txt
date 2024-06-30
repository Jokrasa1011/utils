cmake_minimum_required(VERSION 3.5)
project(move_slow_and_clear)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(cmake_modules REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_core REQUIRED)
find_package(thread REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(rclcpp REQUIRED)
find_package(pluginlib REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${costmap_2d_INCLUDE_DIRS}
  ${cmake_modules_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
  ${nav_core_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS} ${thread_INCLUDE_DIRS}
  ${Eigen3_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${costmap_2d_LIBRARIES}
  ${cmake_modules_LIBRARIES} ${geometry_msgs_LIBRARIES} ${nav_core_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${thread_LIBRARIES} ${Eigen3_LIBRARIES}
  ${rclcpp_LIBRARIES} ${pluginlib_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${costmap_2d_LIBRARIES}
  ${cmake_modules_LIBRARIES} ${geometry_msgs_LIBRARIES} ${nav_core_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${thread_LIBRARIES} ${Eigen3_LIBRARIES}
  ${rclcpp_LIBRARIES} ${pluginlib_LIBRARIES})

remove_definitions(-DDISABLE_LIBUSB-1.0)
add_definitions(${EIGEN3_DEFINITIONS})


add_library(${PROJECT_NAME} src/move_slow_and_clear.cpp)
add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})

## Install project namespaced headers
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  FILES_MATCHING
  PATTERN "*.h"
  PATTERN ".svn"
  EXCLUDE)

install(TARGETS move_slow_and_clear
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(FILES recovery_plugin.xml
  DESTINATION share/${PROJECT_NAME})



ament_export_dependencies(ament_cmake)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(cmake_modules)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(nav_core)
ament_export_dependencies(thread)
ament_export_dependencies(Eigen3)
ament_export_dependencies(rclcpp)
ament_export_dependencies(pluginlib)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${PROJECT_NAME} ${LIBS})

ament_package()
