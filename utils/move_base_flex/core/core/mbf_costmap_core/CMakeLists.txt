cmake_minimum_required(VERSION 3.5)
project(mbf_costmap_core)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(mbf_utility REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(mbf_abstract_core REQUIRED)
find_package(std_msgs REQUIRED)
find_package(nav_core REQUIRED)
find_package(tf2 REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${mbf_utility_INCLUDE_DIRS}
  ${costmap_2d_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
  ${mbf_abstract_core_INCLUDE_DIRS} ${std_msgs_INCLUDE_DIRS}
  ${nav_core_INCLUDE_DIRS} ${tf2_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${mbf_utility_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${mbf_abstract_core_LIBRARIES} ${std_msgs_LIBRARIES} ${nav_core_LIBRARIES}
  ${tf2_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${mbf_utility_LIBRARIES}
  ${costmap_2d_LIBRARIES} ${geometry_msgs_LIBRARIES}
  ${mbf_abstract_core_LIBRARIES} ${std_msgs_LIBRARIES} ${nav_core_LIBRARIES}
  ${tf2_LIBRARIES})

## Install project namespaced headers
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  FILES_MATCHING
  PATTERN "*.h"
  PATTERN ".svn"
  EXCLUDE)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(mbf_utility)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(mbf_abstract_core)
ament_export_dependencies(std_msgs)
ament_export_dependencies(nav_core)
ament_export_dependencies(tf2)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
