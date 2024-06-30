cmake_minimum_required(VERSION 3.5)
project(navfn)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


include(CheckIncludeFile)


add_definitions(${EIGEN3_DEFINITIONS})


# services



check_include_file(sys/time.h HAVE_SYS_TIME_H)
if(HAVE_SYS_TIME_H)
  add_definitions(-DHAVE_SYS_TIME_H)
endif(HAVE_SYS_TIME_H)

add_library(navfn src/navfn.cpp src/navfn_ros.cpp)
add_dependencies(navfn ${PROJECT_NAME}_generate_messages_cpp
  ${catkin_EXPORTED_TARGETS})

add_executable(navfn_node src/navfn_node.cpp)

install(TARGETS navfn_node RUNTIME DESTINATION bin)

install(TARGETS navfn
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/navfn/
  DESTINATION include/${PROJECT_NAME})

install(FILES bgp_plugin.xml DESTINATION share/${PROJECT_NAME})

### The problem with FindFLTK is that it only reports success if *all*
### fltk components are installed, but we only need the core library.
# include (FindFLTK)
include(CheckIncludeFileCXX)
check_include_file_cxx(FL/Fl.H NAVFN_HAVE_FLTK)
check_include_file_cxx(pgm.h NAVFN_HAVE_NETPBM)
message(STATUS
  "NAVFN_HAVE_FLTK: ${NAVFN_HAVE_FLTK}, NETPBM: ${NAVFN_HAVE_NETPBM}")
# Just linking -lfltk is not sufficient on OS X
if(NAVFN_HAVE_FLTK AND NAVFN_HAVE_NETPBM AND NOT APPLE)
  message(STATUS "FLTK found: adding navtest to build")
  add_executable(navtest src/navtest/navtest.cpp src/navtest/navwin.cpp)
  find_package(ament_cmake REQUIRED)
  find_package(FLTK REQUIRED)
  find_package(ros2_console REQUIRED)
  find_package(Eigen3 REQUIRED)
  find_package(pluginlib REQUIRED)
  find_package(costmap_2d REQUIRED)
  find_package(nav_msgs REQUIRED)
  find_package(nav_core REQUIRED)
  find_package(cmake_modules REQUIRED)
  find_package(tf2_ros REQUIRED)
  find_package(sensor_msgs REQUIRED)
  find_package(rclcpp REQUIRED)
  find_package(rosidl_default_generators REQUIRED)
  find_package(geometry_msgs REQUIRED)
  find_package(visualization_msgs REQUIRED)
  set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${FLTK_INCLUDE_DIRS}
    ${ros2_console_INCLUDE_DIRS} ${Eigen3_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS}
    ${costmap_2d_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS} ${nav_core_INCLUDE_DIRS}
    ${cmake_modules_INCLUDE_DIRS} ${tf2_ros_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS}
    ${sensor_msgs_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}
    ${rosidl_default_generators_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS}
    ${visualization_msgs_INCLUDE_DIRS})
  include_directories(${INCLUDE_DIRS})
  set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${FLTK_LIBRARIES}
    ${ros2_console_LIBRARIES} ${Eigen3_LIBRARIES} ${pluginlib_LIBRARIES}
    ${costmap_2d_LIBRARIES} ${nav_msgs_LIBRARIES} ${nav_core_LIBRARIES}
    ${cmake_modules_LIBRARIES} ${tf2_ros_LIBRARIES} ${REQUIRED_LIBRARIES}
    ${sensor_msgs_LIBRARIES} ${rclcpp_LIBRARIES}
    ${rosidl_default_generators_LIBRARIES} ${geometry_msgs_LIBRARIES}
    ${visualization_msgs_LIBRARIES})
  target_link_libraries(navfn_node ${LIBRARY_DIRS})
  target_link_libraries(navtest ${LIBRARY_DIRS})
  set(LIBS ${ament_cmake_LIBRARIES} ${FLTK_LIBRARIES} ${ros2_console_LIBRARIES}
    ${Eigen3_LIBRARIES} ${pluginlib_LIBRARIES} ${costmap_2d_LIBRARIES}
    ${nav_msgs_LIBRARIES} ${nav_core_LIBRARIES} ${cmake_modules_LIBRARIES}
    ${tf2_ros_LIBRARIES} ${REQUIRED_LIBRARIES} ${sensor_msgs_LIBRARIES}
    ${rclcpp_LIBRARIES} ${rosidl_default_generators_LIBRARIES}
    ${geometry_msgs_LIBRARIES} ${visualization_msgs_LIBRARIES})
  rosidl_generate_interfaces(${PROJECT_NAME} "srv/srv" "srv/FILES"
    "srv/MakeNavPlan.srv" "srv/SetCostmap.srv"
    DEPENDENCIES builtin_interfaces nav_msgs sensor_msgs geometry_msgs
    visualization_msgs)
  set(FLTK_SKIP_FLUID 1)
  set(FLTK_SKIP_FORMS 1)
  set(FLTK_SKIP_IMAGES 1)
  if(FLTK_FOUND)
  else(FLTK_FOUND)
  endif(FLTK_FOUND)
else(NAVFN_HAVE_FLTK)
  message(STATUS "FLTK orf NETPBM not found: cannot build navtest")
endif(NAVFN_HAVE_FLTK AND NAVFN_HAVE_NETPBM AND NOT APPLE)

### For some reason (on cmake-2.4.7 at least) the "check" for pgm.h
### always succeeds, even if pgm.h is not installed. It seems to be
### caused by a bug in the rule that attempts to build the C source:
### instead of directly calling e.g. 'gcc -c
### /CMakeFiles/CMakeTmp/CheckIncludeFile.c' it goes through some make
### infrastructure, which reports "Nothing to be done for
### `CMakeFiles/cmTryCompileExec.dir/build'" and calls that a success.
###
### As a workaround we simply force everyone to install libnetpbm
#
# include (CheckIncludeFile)
# check_include_file (pgm.h NAVFN_HAVE_NETPBM)
# message (STATUS "NAVFN_HAVE_NETPBM: ${NAVFN_HAVE_NETPBM}")
# if (NAVFN_HAVE_NETPBM)
#   message (STATUS "found pgm.h")
#   add_definitions (-DNAVFN_HAVE_NETPBM)
#target_link_libraries (navfn -lnetpbm)
# else (NAVFN_HAVE_NETPBM)
#   message (STATUS "pgm.h not found (optional)")
# endif (NAVFN_HAVE_NETPBM)

if(CATKIN_ENABLE_TESTING)
  add_subdirectory(test)
endif()

ament_export_dependencies(ament_cmake)
ament_export_dependencies(FLTK)
ament_export_dependencies(ros2_console)
ament_export_dependencies(Eigen3)
ament_export_dependencies(pluginlib)
ament_export_dependencies(costmap_2d)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(nav_core)
ament_export_dependencies(cmake_modules)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(sensor_msgs)
ament_export_dependencies(rclcpp)
ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(visualization_msgs)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(navfn ${LIBS})

ament_package()
