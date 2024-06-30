cmake_minimum_required(VERSION 3.5)
project(amcl)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


include(CheckIncludeFile)
include(CheckSymbolExists)



# dynamic reconfigure
generate_dynamic_reconfigure_options(cfg/AMCL.cfg)



check_include_file(unistd.h HAVE_UNISTD_H)
if(HAVE_UNISTD_H)
  add_definitions(-DHAVE_UNISTD_H)
endif(HAVE_UNISTD_H)

check_symbol_exists(drand48 stdlib.h HAVE_DRAND48)
if(HAVE_DRAND48)
  add_definitions(-DHAVE_DRAND48)
endif(HAVE_DRAND48)

add_library(amcl_pf src/amcl/pf/pf.c src/amcl/pf/pf_kdtree.c
  src/amcl/pf/pf_pdf.c src/amcl/pf/pf_vector.c src/amcl/pf/eig3.c
  src/amcl/pf/pf_draw.c)

add_library(amcl_map src/amcl/map/map.c src/amcl/map/map_cspace.cpp
  src/amcl/map/map_range.c src/amcl/map/map_store.c src/amcl/map/map_draw.c)

add_library(amcl_sensors src/amcl/sensors/amcl_sensor.cpp
  src/amcl/sensors/amcl_odom.cpp src/amcl/sensors/amcl_laser.cpp)


add_executable(amcl src/amcl_node.cpp)
find_package(ament_cmake REQUIRED)
find_package(message_filters REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(Boost REQUIRED)
find_package(rosbag REQUIRED)
find_package(tf2_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_srvs REQUIRED)
find_package(rostest REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(diagnostic_updater REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(tf2 REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS} ${message_filters_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS} ${rosbag_INCLUDE_DIRS}
  ${tf2_msgs_INCLUDE_DIRS} ${nav_msgs_INCLUDE_DIRS} ${rclcpp_INCLUDE_DIRS}
  ${std_srvs_INCLUDE_DIRS} ${rostest_INCLUDE_DIRS} ${sensor_msgs_INCLUDE_DIRS}
  ${tf2_ros_INCLUDE_DIRS} ${REQUIRED_INCLUDE_DIRS}
  ${diagnostic_updater_INCLUDE_DIRS} ${tf2_geometry_msgs_INCLUDE_DIRS}
  ${tf2_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES} ${message_filters_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${Boost_LIBRARIES} ${rosbag_LIBRARIES}
  ${tf2_msgs_LIBRARIES} ${nav_msgs_LIBRARIES} ${rclcpp_LIBRARIES}
  ${std_srvs_LIBRARIES} ${rostest_LIBRARIES} ${sensor_msgs_LIBRARIES}
  ${tf2_ros_LIBRARIES} ${REQUIRED_LIBRARIES} ${diagnostic_updater_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${tf2_LIBRARIES})
target_link_libraries(amcl ${LIBRARY_DIRS})
set(LIBS ${ament_cmake_LIBRARIES} ${message_filters_LIBRARIES}
  ${geometry_msgs_LIBRARIES} ${Boost_LIBRARIES} ${rosbag_LIBRARIES}
  ${tf2_msgs_LIBRARIES} ${nav_msgs_LIBRARIES} ${rclcpp_LIBRARIES}
  ${std_srvs_LIBRARIES} ${rostest_LIBRARIES} ${sensor_msgs_LIBRARIES}
  ${tf2_ros_LIBRARIES} ${REQUIRED_LIBRARIES} ${diagnostic_updater_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES} ${tf2_LIBRARIES})
add_dependencies(amcl ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS})


install(TARGETS amcl RUNTIME DESTINATION bin)

install(TARGETS amcl_sensors amcl_map amcl_pf
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(DIRECTORY include/amcl/
  DESTINATION include/${PROJECT_NAME})

install(DIRECTORY examples/
  DESTINATION share/${PROJECT_NAME}/examples)

## Configure Tests
if(CATKIN_ENABLE_TESTING)

  # Bags
  catkin_download_test_data(${PROJECT_NAME}_basic_localization_stage_indexed.bag
    http://download.ros.org/data/amcl/basic_localization_stage_indexed.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    41fe43af189ec71e5e48eb9ed661a655)
  catkin_download_test_data(${PROJECT_NAME}_global_localization_stage_indexed.bag
    http://download.ros.org/data/amcl/global_localization_stage_indexed.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    752f711cf4f6e8d1d660675e2da096b0)
  catkin_download_test_data(${PROJECT_NAME}_small_loop_prf_indexed.bag
    http://download.ros.org/data/amcl/small_loop_prf_indexed.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    e4ef0fc006872b43f12ed8a7ce7dcd81)
  catkin_download_test_data(
    ${PROJECT_NAME}_small_loop_crazy_driving_prg_indexed.bag
    http://download.ros.org/data/amcl/small_loop_crazy_driving_prg_indexed.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    4a58d1a7962914009d99000d06e5939c)
  catkin_download_test_data(${PROJECT_NAME}_texas_greenroom_loop_indexed.bag
    http://download.ros.org/data/amcl/texas_greenroom_loop_indexed.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    6e3432115cccdca1247f6c807038e13d)
  catkin_download_test_data(${PROJECT_NAME}_texas_willow_hallway_loop_indexed.bag
    http://download.ros.org/data/amcl/texas_willow_hallway_loop_indexed.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    27deb742fdcd3af44cf446f39f2688a8)
  catkin_download_test_data(${PROJECT_NAME}_rosie_localization_stage.bag
    http://download.ros.org/data/amcl/rosie_localization_stage.bag
    DESTINATION share/${PROJECT_NAME}/test MD5
    3347bf3835724cfa45e958c5c1846066)

  # Maps
  catkin_download_test_data(${PROJECT_NAME}_willow-full.pgm
    http://download.ros.org/data/amcl/willow-full.pgm
    DESTINATION share/${PROJECT_NAME}/test MD5
    b84465cdbbfe3e2fb9eb4579e0bcaf0e)
  catkin_download_test_data(${PROJECT_NAME}_willow-full-0.05.pgm
    http://download.ros.org/data/amcl/willow-full-0.05.pgm
    DESTINATION share/${PROJECT_NAME}/test MD5
    b61694296e08965096c5e78611fd9765)

  # Tests
  add_rostest(test/set_initial_pose.xml)
  add_rostest(test/set_initial_pose_delayed.xml)
  add_rostest(test/basic_localization_stage.xml)
  add_rostest(test/global_localization_stage.xml)
  add_rostest(test/small_loop_prf.xml)
  add_rostest(test/small_loop_crazy_driving_prg.xml)
  add_rostest(test/texas_greenroom_loop.xml)
  add_rostest(test/rosie_multilaser.xml)
  add_rostest(test/texas_willow_hallway_loop.xml)
endif()

ament_export_dependencies(ament_cmake)
ament_export_dependencies(message_filters)
ament_export_dependencies(geometry_msgs)
ament_export_dependencies(Boost)
ament_export_dependencies(rosbag)
ament_export_dependencies(tf2_msgs)
ament_export_dependencies(nav_msgs)
ament_export_dependencies(rclcpp)
ament_export_dependencies(std_srvs)
ament_export_dependencies(rostest)
ament_export_dependencies(sensor_msgs)
ament_export_dependencies(tf2_ros)
ament_export_dependencies(diagnostic_updater)
ament_export_dependencies(tf2_geometry_msgs)
ament_export_dependencies(tf2)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(amcl_pf amcl_map amcl_sensors ${LIBS})

ament_package()
