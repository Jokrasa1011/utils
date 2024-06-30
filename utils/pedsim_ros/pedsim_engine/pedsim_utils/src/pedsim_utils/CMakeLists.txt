cmake_minimum_required(VERSION 3.5)
project(pedsim_utils)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

add_compile_options(-Wall -Wunused -std=c++11)

set(PACKAGE_DEPS cmake_modules geometry_msgs pedsim_msgs roscpp rospy)

find_package(ament_cmake REQUIRED)
find_package(${PACKAGE_DEPS} REQUIRED)
find_package(Eigen3 REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS}
  ${${PACKAGE_DEPS}_INCLUDE_DIRS} ${Eigen3_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${REQUIRED_LIBRARIES}
  ${${PACKAGE_DEPS}_LIBRARIES} ${Eigen3_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${REQUIRED_LIBRARIES}
  ${${PACKAGE_DEPS}_LIBRARIES} ${Eigen3_LIBRARIES})
###################################
## catkin specific configuration ##
###################################

###########
## Build ##
###########

set(LIBRARY_NAME ${PROJECT_NAME})
add_library(${LIBRARY_NAME} src/${PROJECT_NAME}/geometry.cpp
  src/${PROJECT_NAME}/pedsim_utils.cpp)

add_dependencies(${LIBRARY_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})


#############
## Install ##
#############

## Mark executables and/or libraries for installation
install(TARGETS ${LIBRARY_NAME}
  LIBRARY
  DESTINATION lib)

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_pedsim_utils.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(${PACKAGE_DEPS})
ament_export_dependencies(Eigen3)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${LIBRARY_NAME} ${LIBS})

ament_package()
