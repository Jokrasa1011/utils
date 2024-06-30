cmake_minimum_required(VERSION 3.5)
project(pedsim)

#------------------ Configuration ------------------#
option(SHALL_DEBUG "Enable debug features" OFF)
option(SHALL_PROFILE "Enable the code profiling feature" OFF)
option(CMAKE_VERBOSE_MAKEFILE "Full compiler output" ON)


#----------------- Compiler Flags ------------------#
add_definitions(-Wall -Wunused -std=c++14 -pipe)

#debugging
if(SHALL_DEBUG)
  message("Debugging activated")
  add_definitions(-O0 -DDEBUG -ggdb -g3 -rdynamic)
else(SHALL_DEBUG)
  message("Debugging deactivated")
  add_definitions(-Os)
endif(SHALL_DEBUG)



find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(Boost REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES} ${Boost_LIBRARIES}
  ${REQUIRED_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${rclcpp_LIBRARIES} ${Boost_LIBRARIES}
  ${REQUIRED_LIBRARIES})


set(SOURCES src/ped_agent.cpp src/ped_angle.cpp src/ped_obstacle.cpp
  src/ped_scene.cpp src/ped_tree.cpp src/ped_vector.cpp src/ped_waypoint.cpp
  src/types.cpp)

add_library(pedsim ${SOURCES})


ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_dependencies(Boost)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(pedsim ${LIBS})

ament_package()
