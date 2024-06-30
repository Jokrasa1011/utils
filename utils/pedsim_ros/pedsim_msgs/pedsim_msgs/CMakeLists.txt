cmake_minimum_required(VERSION 3.5)
project(pedsim_msgs)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


# message and service dependencies
set(MESSAGE_DEPENDENCIES std_msgs geometry_msgs sensor_msgs nav_msgs)


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
rosidl_generate_interfaces(${PROJECT_NAME} "msg/msg" "msg/FILES"
  "msg/AgentState.msg" "msg/AgentStates.msg" "msg/AgentGroup.msg"
  "msg/AgentGroups.msg" "msg/AgentForce.msg" "msg/Wall.msg" "msg/Walls.msg"
  "msg/TrackedPerson.msg" "msg/TrackedPersons.msg" "msg/TrackedGroup.msg"
  "msg/TrackedGroups.msg" "msg/SocialRelation.msg" "msg/SocialRelations.msg"
  "msg/SocialActivity.msg" "msg/SocialActivities.msg" "msg/Waypoint.msg"
  "msg/Waypoints.msg" "msg/Ped.msg" "msg/Obstacle.msg" "msg/Obstacles.msg"
  "msg/RobotState.msg" "msg/PedsimAgentsDataframe.msg" "msg/AgentFeedback.msg"
  "msg/AgentFeedbacks.msg"
  DEPENDENCIES builtin_interfaces)

## Generate messages in the 'msg' folder

# generate the messages


#Declare package run-time dependencies

ament_export_dependencies(ament_cmake)
ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(${MESSAGE_DEPENDENCIES})
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
