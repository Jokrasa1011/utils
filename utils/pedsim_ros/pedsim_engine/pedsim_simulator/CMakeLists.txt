cmake_minimum_required(VERSION 3.5)
project(pedsim_simulator)
add_definitions(-Wall -Wunused -std=c++14 -pipe -Wunused -Wextra)
set(PEDSIM_SIMULATOR_DEPENDENCIES roscpp rospy std_msgs pedsim pedsim_msgs
  pedsim_srvs pedsim_utils std_srvs geometry_msgs nav_msgs tf cmake_modules
  dynamic_reconfigure flatland_msgs roslib)

# Declaration of package required
pkg_check_modules(YAMLCPP REQUIRED yaml-cpp)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

## Find catkin macros and libraries

# dynamic reconfigure parameters
generate_dynamic_reconfigure_options(config/PedsimSimulator.cfg)


add_definitions(${Qt5Widgets_DEFINITIONS})

set(SOURCES src/simulator_node.cpp src/simulator.cpp src/scene.cpp
  src/config.cpp src/agentstatemachine.cpp src/scenarioreader.cpp src/rng.cpp
  src/scene_services.cpp src/agent_pose_stamped.cpp  # elements
  src/element/agent.cpp src/element/agentgroup.cpp src/element/agentcluster.cpp
  src/element/areawaypoint.cpp src/element/attractionarea.cpp
  src/element/queueingwaypoint.cpp src/element/waitingqueue.cpp
  src/element/waypoint.cpp src/element/wall.cpp src/element/scenarioelement.cpp
  src/element/robot.cpp  # forces
  src/force/alongwallforce.cpp src/force/force.cpp
  src/force/groupcoherenceforce.cpp src/force/groupgazeforce.cpp
  src/force/grouprepulsionforce.cpp src/force/randomforce.cpp  # waypointplanner
  src/waypointplanner/individualwaypointplanner.cpp
  src/waypointplanner/queueingplanner.cpp src/waypointplanner/shoppingplanner.cpp
  src/waypointplanner/groupwaypointplanner.cpp)


set(MOC_FILES include/pedsim_simulator/config.h include/pedsim_simulator/scene.h
  include/pedsim_simulator/agentstatemachine.h
  include/pedsim_simulator/scene_services.h
  include/pedsim_simulator/agent_pose_stamped.h
  include/pedsim_simulator/element/scenarioelement.h
  include/pedsim_simulator/element/robot.h
  include/pedsim_simulator/element/agent.h
  include/pedsim_simulator/element/agentcluster.h
  include/pedsim_simulator/element/agentgroup.h
  include/pedsim_simulator/element/attractionarea.h
  include/pedsim_simulator/element/obstacle.h
  include/pedsim_simulator/element/wall.h
  include/pedsim_simulator/element/waypoint.h
  include/pedsim_simulator/element/areawaypoint.h
  include/pedsim_simulator/element/waitingqueue.h
  include/pedsim_simulator/element/queueingwaypoint.h
  include/pedsim_simulator/force/force.h
  include/pedsim_simulator/force/randomforce.h
  include/pedsim_simulator/force/groupgazeforce.h
  include/pedsim_simulator/force/groupcoherenceforce.h
  include/pedsim_simulator/force/grouprepulsionforce.h
  include/pedsim_simulator/force/alongwallforce.h
  include/pedsim_simulator/waypointplanner/waypointplanner.h
  include/pedsim_simulator/waypointplanner/individualwaypointplanner.h
  include/pedsim_simulator/waypointplanner/groupwaypointplanner.h
  include/pedsim_simulator/waypointplanner/shoppingplanner.h
  include/pedsim_simulator/waypointplanner/queueingplanner.h)
qt5_wrap_cpp(MOC_SRCS_UI ${MOC_FILES})

set(EXECUTABLE_NAME ${PROJECT_NAME})
add_executable(${EXECUTABLE_NAME} ${SOURCES} ${MOC_SRCS_UI})
add_dependencies(${EXECUTABLE_NAME} ${catkin_EXPORTED_TARGETS})
add_dependencies(${EXECUTABLE_NAME} ${PROJECT_NAME}_gencfg)

add_executable(simulate_diff_drive_robot src/simulate_diff_drive_robot.cpp)
find_package(ament_cmake REQUIRED)
find_package(Qt5Widgets REQUIRED)
find_package(${PEDSIM_SIMULATOR_DEPENDENCIES} REQUIRED)
find_package(Boost REQUIRED)
find_package(PkgConfig REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${Qt5Widgets_INCLUDE_DIRS}
  ${REQUIRED_INCLUDE_DIRS} ${${PEDSIM_SIMULATOR_DEPENDENCIES}_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS} ${PkgConfig_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${Qt5Widgets_LIBRARIES}
  ${REQUIRED_LIBRARIES} ${${PEDSIM_SIMULATOR_DEPENDENCIES}_LIBRARIES}
  ${Boost_LIBRARIES} ${PkgConfig_LIBRARIES})
target_link_libraries(${EXECUTABLE_NAME} ${LIBRARY_DIRS})
target_link_libraries(simulate_diff_drive_robot ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${Qt5Widgets_LIBRARIES} ${REQUIRED_LIBRARIES}
  ${${PEDSIM_SIMULATOR_DEPENDENCIES}_LIBRARIES} ${Boost_LIBRARIES}
  ${PkgConfig_LIBRARIES})
add_dependencies(simulate_diff_drive_robot ${catkin_EXPORTED_TARGETS})

install(TARGETS ${EXECUTABLE_NAME} simulate_diff_drive_robot
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME})


## Unit Tests

ament_export_dependencies(ament_cmake)
ament_export_dependencies(Qt5Widgets)
ament_export_dependencies(${PEDSIM_SIMULATOR_DEPENDENCIES})
ament_export_dependencies(Boost)
ament_export_dependencies(PkgConfig)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
