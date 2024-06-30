cmake_minimum_required(VERSION 3.5)
project(pedsim_visualizer)
add_definitions(-Wall -Wunused -std=c++14 -pipe -Wunused -Wextra)

set(PACKAGE_DEPS geometry_msgs pedsim_msgs pedsim_utils roscpp rospy std_msgs
  visualization_msgs dynamic_reconfigure)

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

generate_dynamic_reconfigure_options(config/PedsimVisualizer.cfg)

###################################
## catkin specific configuration ##
###################################

###########
## Build ##
###########
link_directories(${catkin_LIBRARY_DIRS})

set(EXECUTABLE_NAME ${PROJECT_NAME}_node)
add_executable(${EXECUTABLE_NAME} src/sim_visualizer_node.cpp
  src/sim_visualizer.cpp)
find_package(ament_cmake REQUIRED)
find_package(${PACKAGE_DEPS} REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${${PACKAGE_DEPS}_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${${PACKAGE_DEPS}_LIBRARIES})
target_link_libraries(${EXECUTABLE_NAME} ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${${PACKAGE_DEPS}_LIBRARIES})

add_dependencies(${EXECUTABLE_NAME} ${catkin_EXPORTED_TARGETS})
add_dependencies(${EXECUTABLE_NAME} ${PROJECT_NAME}_gencfg)


#############
## Install ##
#############

## Mark executables and/or libraries for installation
install(TARGETS ${EXECUTABLE_NAME}
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

## Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  FILES_MATCHING
  PATTERN "*.h"
  PATTERN ".svn"
  EXCLUDE)


#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_pedsim_visualizer.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(${PACKAGE_DEPS})
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
