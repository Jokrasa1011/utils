cmake_minimum_required(VERSION 3.5)
project(flatland_viz)

# Get the LSB release name (14.04 or 16.04) string into variable ${LSB_RELEASE_VALUE}
find_program(LSB_RELEASE_EXECUTABLE lsb_release)
execute_process(COMMAND ${LSB_RELEASE_EXECUTABLE} -s -r
  OUTPUT_VARIABLE
  LSB_RELEASE_VALUE
  OUTPUT_STRIP_TRAILING_WHITESPACE)

if(${LSB_RELEASE_VALUE} STREQUAL "14.04")
  message("Skipping flatland_viz because it is incompatible with 14.04")
  return()
endif()

# Ensure we're using c++11
set(CMAKE_CXX_FLAGS -std=c++14)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

##############
## coverage ##
##############

set(COVERAGE "OFF" CACHE STRING "Enable coverage generation.")

message(STATUS "Using COVERAGE: ${COVERAGE}")
if("${COVERAGE}" STREQUAL "ON")
  set(CMAKE_CXX_FLAGS
    "${CMAKE_CXX_FLAGS} --coverage -fprofile-arcs -ftest-coverage")
endif()

########################
## Ogre Include Stuff ##
########################


pkg_check_modules(OGRE_OV OGRE OGRE-Overlay)

# Old versions of OGRE (pre 1.9) included OGRE-Overlay in the main package
# (i.e. there was no OGRE-Overlay component).  So if the above
# pkg_check_modules() failed, try looking for just OGRE.
if(NOT OGRE_OV_FOUND)
  pkg_check_modules(OGRE_OV REQUIRED OGRE)
endif(NOT OGRE_OV_FOUND)

###################################
## catkin specific configuration ##
###################################


###########
## Build ##
###########

link_directories(${catkin_LIBRARY_DIRS})

## This setting causes Qt's "MOC" generation to happen automatically.
set(CMAKE_AUTOMOC ON)

## This plugin includes Qt widgets, so we must include Qt.
## We'll use the version that rviz used so they are compatible.
if(rviz_QT_VERSION VERSION_LESS "5")
  message(STATUS "Using Qt4 based on the rviz_QT_VERSION: ${rviz_QT_VERSION}")
  ## pull in all required include dirs, define QT_LIBRARIES, etc.
  include(${QT_USE_FILE})
else()
  message(STATUS "Using Qt5 based on the rviz_QT_VERSION: ${rviz_QT_VERSION}")
  ## make target_link_libraries(${QT_LIBRARIES}) pull in all required dependencies
  set(QT_LIBRARIES Qt5::Widgets)
endif()

add_definitions(-DQT_NO_KEYWORDS)

## Declare a C++ executable
add_executable(flatland_viz src/flatland_viz_node.cpp src/flatland_viz.cpp
  include/flatland_viz/flatland_viz.h src/flatland_window.cpp
  include/flatland_viz/flatland_window.h src/load_model_dialog.cpp
  include/flatland_viz/load_model_dialog.h src/spawn_model_tool.cpp
  include/flatland_viz/spawn_model_tool.h src/pause_sim_tool.cpp
  include/flatland_viz/pause_sim_tool.h)
find_package(ament_cmake REQUIRED)
find_package(QtCore REQUIRED)
find_package(rviz REQUIRED)
find_package(Qt5 REQUIRED)
find_package(flatland_server REQUIRED)
find_package(${rviz_QT_VERSION} REQUIRED)
find_package(Qt4 REQUIRED)
find_package(QtGui REQUIRED)
find_package(Core REQUIRED)
find_package(rostest REQUIRED)
find_package(Widgets REQUIRED)
find_package(rclcpp REQUIRED)
find_package(flatland_msgs REQUIRED)
find_package(EXACT REQUIRED)
find_package(PkgConfig REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${QtCore_INCLUDE_DIRS}
  ${rviz_INCLUDE_DIRS} ${Qt5_INCLUDE_DIRS} ${flatland_server_INCLUDE_DIRS}
  ${${rviz_QT_VERSION}_INCLUDE_DIRS} ${Qt4_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS}
  ${QtGui_INCLUDE_DIRS} ${Core_INCLUDE_DIRS} ${rostest_INCLUDE_DIRS}
  ${Widgets_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS} ${flatland_msgs_INCLUDE_DIRS}
  ${EXACT_INCLUDE_DIRS} ${PkgConfig_INCLUDE_DIRS})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/rosidl_generator_cpp>
  ${CMAKE_CURRENT_SOURCE_DIR}
  ./
)
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${QtCore_LIBRARIES} ${rviz_LIBRARIES}
  ${Qt5_LIBRARIES} ${flatland_server_LIBRARIES} ${${rviz_QT_VERSION}_LIBRARIES}
  ${Qt4_LIBRARIES} ${REQUIRED_LIBRARIES} ${QtGui_LIBRARIES} ${Core_LIBRARIES}
  ${rostest_LIBRARIES} ${Widgets_LIBRARIES} ${rclcpp_LIBRARIES}
  ${flatland_msgs_LIBRARIES} ${EXACT_LIBRARIES} ${PkgConfig_LIBRARIES})
target_link_libraries(flatland_viz
  ${cpp_typesupport_target}
  # ${SDL2_LIBRARIES}
  # ${OPENGL_LIBRARIES}
)
set(LIBS ${ament_cmake_LIBRARIES} ${QtCore_LIBRARIES} ${rviz_LIBRARIES}
  ${Qt5_LIBRARIES} ${flatland_server_LIBRARIES} ${${rviz_QT_VERSION}_LIBRARIES}
  ${Qt4_LIBRARIES} ${REQUIRED_LIBRARIES} ${QtGui_LIBRARIES} ${Core_LIBRARIES}
  ${rostest_LIBRARIES} ${Widgets_LIBRARIES} ${rclcpp_LIBRARIES}
  ${flatland_msgs_LIBRARIES} ${EXACT_LIBRARIES} ${PkgConfig_LIBRARIES})
add_dependencies(flatland_viz ${catkin_EXPORTED_TARGETS})


add_library(flatland_viz_plugins src/load_model_dialog.cpp
  include/flatland_viz/load_model_dialog.h src/spawn_model_tool.cpp
  include/flatland_viz/spawn_model_tool.h src/pause_sim_tool.cpp
  include/flatland_viz/pause_sim_tool.h)

add_dependencies(flatland_viz_plugins ${catkin_EXPORTED_TARGETS})


#############
## Install ##
#############

# Mark executables and/or libraries for installation
install(TARGETS flatland_viz flatland_viz_plugins
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(FILES plugin_description.xml
  DESTINATION share/${PROJECT_NAME})

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)

endif()

ament_export_dependencies(ament_cmake)
ament_export_dependencies(QtCore)
ament_export_dependencies(rviz)
ament_export_dependencies(Qt5)
ament_export_dependencies(flatland_server)
ament_export_dependencies(${rviz_QT_VERSION})
ament_export_dependencies(Qt4)
ament_export_dependencies(QtGui)
ament_export_dependencies(Core)
ament_export_dependencies(rostest)
ament_export_dependencies(Widgets)
ament_export_dependencies(rclcpp)
ament_export_dependencies(flatland_msgs)
ament_export_dependencies(EXACT)
ament_export_dependencies(PkgConfig)
ament_export_target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/rosidl_generator_cpp>
  ${CMAKE_CURRENT_SOURCE_DIR}
  ./
)
ament_export_libraries(flatland_viz_plugins ${LIBS})

ament_package()
