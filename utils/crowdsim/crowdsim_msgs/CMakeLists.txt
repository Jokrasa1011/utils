cmake_minimum_required(VERSION 3.5)
project(crowdsim_msgs)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


# message and service dependencies
set(MESSAGE_DEPENDENCIES std_msgs geometry_msgs sensor_msgs nav_msgs pedsim_msgs)


find_package(ament_cmake REQUIRED)
find_package(${MESSAGE_DEPENDENCIES} REQUIRED)
find_package(rosidl_default_generators REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS}
  ${${MESSAGE_DEPENDENCIES}_INCLUDE_DIRS}
  ${rosidl_default_generators_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${${MESSAGE_DEPENDENCIES}_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${${MESSAGE_DEPENDENCIES}_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES})
rosidl_generate_interfaces(${PROJECT_NAME} "msg/msg" "msg/FILES"
  "msg/SemanticData.msg" "msg/SemanticDatum.msg"
  DEPENDENCIES builtin_interfaces)

# Generate messages in the 'msg' folder

# add_service_files( DIRECTORY srv
#   FILES
# )

# generate the messages


#Declare package run-time dependencies

ament_export_dependencies(ament_cmake)
ament_export_dependencies(${MESSAGE_DEPENDENCIES})
ament_export_dependencies(rosidl_default_generators)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()