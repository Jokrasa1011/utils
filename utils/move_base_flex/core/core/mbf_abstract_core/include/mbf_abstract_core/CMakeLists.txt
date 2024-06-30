cmake_minimum_required(VERSION 3.5)
project(mbf_abstract_core)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
  ${std_msgs_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${std_msgs_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${std_msgs_LIBRARIES})


## Install project namespaced headers
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  FILES_MATCHING
  PATTERN "*.h"
  PATTERN ".svn"
  EXCLUDE)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(std_msgs)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
