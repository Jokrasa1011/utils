cmake_minimum_required(VERSION 3.5)
project(flatland_msgs)

# Ensure we're using c++11
set(CMAKE_CXX_FLAGS -std=c++14)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

find_package(ament_cmake REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${PkgConfig_INCLUDE_DIRS}
  ${rosidl_default_generators_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
  ${REQUIRED_INCLUDE_DIRS} ${std_msgs_INCLUDE_DIRS})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/rosidl_generator_cpp>
  ${CMAKE_CURRENT_SOURCE_DIR}
  ./
)
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${PkgConfig_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${std_msgs_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${PkgConfig_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${std_msgs_LIBRARIES})
rosidl_generate_interfaces(${PROJECT_NAME} "msg/DebugTopicList.msg"
  "msg/Collision.msg" "msg/Collisions.msg" "msg/Vector2.msg" "msg/Model.msg"
  "msg/DangerZone.msg" "msg/StepWorld.msg" "msg/MoveModelMsg.msg"
  "srv/SpawnModel.srv" "srv/SpawnModels.srv" "srv/DeleteModel.srv"
  "srv/DeleteModels.srv" "srv/MoveModel.srv"
  DEPENDENCIES builtin_interfaces geometry_msgs std_msgs)
## System dependencies are found with CMake's conventions

################
## Build MSGS ##
################



###################################
## catkin specific configuration ##
###################################

###########
## Build ##
###########


ament_export_dependencies(ament_cmake)
ament_export_dependencies(PkgConfig)
ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(std_msgs)
ament_export_target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/rosidl_generator_cpp>
  ${CMAKE_CURRENT_SOURCE_DIR}
  ./
)

ament_package()
