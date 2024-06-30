cmake_minimum_required(VERSION 3.5)
project(inter_util)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES})


add_library(inter_util src/inter_util.cpp)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(inter_util ${LIBS})

ament_package()
