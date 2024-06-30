cmake_minimum_required(VERSION 3.5)
project(pedsim_sensors)
add_definitions(-Wall -Wunused -std=c++14 -pipe -Wunused -Wextra)

set(PACKAGE_DEPS geometry_msgs nav_msgs pedsim_msgs roscpp rospy sensor_msgs tf
  pedsim_utils)


###########
## Build ##
###########

link_directories(${catkin_LIBRARY_DIRS})

# People point cloud sensor.
set(PEOPLE_PCD_EXEC_NAME pedsim_people_sensor)
add_executable(${PEOPLE_PCD_EXEC_NAME} src/pedsim_sensors/people_point_cloud.cpp)
add_dependencies(${PEOPLE_PCD_EXEC_NAME} ${catkin_EXPORTED_TARGETS})

# Obstacle point cloud sensor.
set(OBSTACLE_PCD_EXEC_NAME pedsim_obstacle_sensor)
add_executable(${OBSTACLE_PCD_EXEC_NAME}
  src/pedsim_sensors/obstacle_point_cloud.cpp)
add_dependencies(${OBSTACLE_PCD_EXEC_NAME} ${catkin_EXPORTED_TARGETS})

# Point cloud sensor.
set(OCCLUSION_PCD_EXEC_NAME pedsim_occlusion_sensor)
add_executable(${OCCLUSION_PCD_EXEC_NAME}
  src/pedsim_sensors/occlusion_point_cloud.cpp)
find_package(ament_cmake REQUIRED)
find_package(${PACKAGE_DEPS} REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${${PACKAGE_DEPS}_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${${PACKAGE_DEPS}_LIBRARIES})
target_link_libraries(${PEOPLE_PCD_EXEC_NAME} ${LIBRARY_DIRS})
target_link_libraries(${OBSTACLE_PCD_EXEC_NAME} ${LIBRARY_DIRS})
target_link_libraries(${OCCLUSION_PCD_EXEC_NAME} ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${${PACKAGE_DEPS}_LIBRARIES})
add_dependencies(${OCCLUSION_PCD_EXEC_NAME} ${catkin_EXPORTED_TARGETS})

#############
## Install ##
#############

install(TARGETS ${PEOPLE_PCD_EXEC_NAME} ${OBSTACLE_PCD_EXEC_NAME}
  ${OCCLUSION_PCD_EXEC_NAME}
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
# catkin_add_gtest(${PROJECT_NAME}-test test/test_pedsim_sensors.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(${PACKAGE_DEPS})
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
