cmake_minimum_required(VERSION 3.5)
project(mbf_msgs)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(actionlib_msgs REQUIRED)
find_package(genmsg REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(std_msgs REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
  ${actionlib_msgs_INCLUDE_DIRS} ${genmsg_INCLUDE_DIRS}
  ${rosidl_default_generators_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS}
  ${std_msgs_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${actionlib_msgs_LIBRARIES} ${genmsg_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${std_msgs_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${actionlib_msgs_LIBRARIES} ${genmsg_LIBRARIES}
  ${rosidl_default_generators_LIBRARIES} ${nav_msgs_LIBRARIES}
  ${std_msgs_LIBRARIES})
rosidl_generate_interfaces(${PROJECT_NAME} "srv/srv" "srv/FILES"
  "srv/CheckPoint.srv" "srv/CheckPose.srv" "srv/CheckPath.srv"
  "srv/FindValidPose.srv"
  DEPENDENCIES builtin_interfaces geometry_msgs actionlib_msgs nav_msgs std_msgs)

add_action_files(DIRECTORY action
  FILES GetPath.action GetInterPath.action ExePath.action Recovery.action
  MoveBase.action)



ament_export_dependencies(ament_cmake)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(actionlib_msgs)
ament_export_dependencies(genmsg)
ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(std_msgs)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
