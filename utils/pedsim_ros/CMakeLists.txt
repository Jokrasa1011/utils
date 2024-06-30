cmake_minimum_required(VERSION 3.5)
project(pedsim_ros)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${catkin_INCLUDE_DIRS}
  ${REQUIRED_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${catkin_LIBRARIES}
  ${REQUIRED_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${catkin_LIBRARIES} ${REQUIRED_LIBRARIES})

ament_export_dependencies(ament_cmake)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
