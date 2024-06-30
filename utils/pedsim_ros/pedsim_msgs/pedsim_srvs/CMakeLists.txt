cmake_minimum_required(VERSION 3.5)
project(pedsim_srvs)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



set(MESSAGE_DEPENDENCIES pedsim_msgs std_msgs)


find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(${MESSAGE_DEPENDENCIES} REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS}
  ${rosidl_default_generators_INCLUDE_DIRS}
  ${${MESSAGE_DEPENDENCIES}_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${rosidl_default_generators_LIBRARIES}
  ${${MESSAGE_DEPENDENCIES}_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${rosidl_default_generators_LIBRARIES}
  ${${MESSAGE_DEPENDENCIES}_LIBRARIES})
rosidl_generate_interfaces(${PROJECT_NAME} "srv/srv" "srv/FILES"
  "srv/SetAgentState.srv" "srv/GetAgentState.srv" "srv/SetAllAgentsState.srv"
  "srv/GetAllAgentsState.srv" "srv/SpawnPed.srv" "srv/SpawnPeds.srv"
  "srv/SpawnWalls.srv" "srv/MovePeds.srv" "srv/SpawnObstacles.srv"
  "srv/RegisterRobot.srv"
  DEPENDENCIES builtin_interfaces)
link_directories(${catkin_LIBRARY_DIRS})


# the services


#add_dependencies(some_target ${PROJECT_NAME}_gencpp)


ament_export_dependencies(ament_cmake)
ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(${MESSAGE_DEPENDENCIES})
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
