cmake_minimum_required(VERSION 3.5)
project(clear_costmap_recovery)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
find_package(costmap_2d REQUIRED)
find_package(cmake_modules REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(rostest REQUIRED)
find_package(rclcpp REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(pluginlib REQUIRED)
find_package(nav_core REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${costmap_2d_INCLUDE_DIRS}
  ${cmake_modules_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS}
  ${rostest_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS} ${Eigen3_INCLUDE_DIRS}
  ${pluginlib_INCLUDE_DIRS} ${nav_core_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${costmap_2d_LIBRARIES}
  ${cmake_modules_LIBRARIES} ${REQUIRED_LIBRARIES} ${tf2_ros_LIBRARIES}
  ${rostest_LIBRARIES} ${rclcpp_LIBRARIES} ${Eigen3_LIBRARIES}
  ${pluginlib_LIBRARIES} ${nav_core_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${costmap_2d_LIBRARIES}
  ${cmake_modules_LIBRARIES} ${REQUIRED_LIBRARIES} ${tf2_ros_LIBRARIES}
  ${rostest_LIBRARIES} ${rclcpp_LIBRARIES} ${Eigen3_LIBRARIES}
  ${pluginlib_LIBRARIES} ${nav_core_LIBRARIES})
remove_definitions(-DDISABLE_LIBUSB-1.0)
add_definitions(${EIGEN3_DEFINITIONS})


add_library(clear_costmap_recovery src/clear_costmap_recovery.cpp)
add_dependencies(clear_costmap_recovery ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})


## Configure Tests
if(CATKIN_ENABLE_TESTING)
  # Find package test dependencies

  # Add the test folder to the include directories

  # Create targets for test executables
  add_rostest_gtest(clear_tester test/clear_tests.launch test/clear_tester.cpp)
endif()


install(TARGETS clear_costmap_recovery
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(FILES ccr_plugin.xml DESTINATION share/${PROJECT_NAME})

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
  PATTERN ".svn"
  EXCLUDE)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(cmake_modules)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(rostest)
ament_export_dependencies(rclcpp)
ament_export_dependencies(Eigen3)
ament_export_dependencies(pluginlib)
ament_export_dependencies(nav_core)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(clear_costmap_recovery ${LIBS})

ament_package()
