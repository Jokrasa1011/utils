# Software License Agreement (BSD License)
#
#  Copyright (c) 2013-2015, Timm Linder, Social Robotics Lab, University of Freiburg
#  Copyright (c) 2012, Willow Garage, Inc.
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#  * Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


cmake_minimum_required(VERSION 3.5)
project(spencer_tracking_rviz_plugin)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


find_package(ament_cmake REQUIRED)
find_package(spencer_social_relation_msgs REQUIRED)
find_package(EXACT REQUIRED)
find_package(QtCore REQUIRED)
find_package(Qt5 REQUIRED)
find_package(spencer_tracking_msgs REQUIRED)
find_package(${rviz_QT_VERSION} REQUIRED)
find_package(spencer_human_attribute_msgs REQUIRED)
find_package(Core REQUIRED)
find_package(Widgets REQUIRED)
find_package(Qt4 REQUIRED)
find_package(QtGui REQUIRED)
find_package(rviz REQUIRED)
find_package(pedsim REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS}
  ${spencer_social_relation_msgs_INCLUDE_DIRS} ${EXACT_INCLUDE_DIRS}
  ${QtCore_INCLUDE_DIRS} ${Qt5_INCLUDE_DIRS} ${spencer_tracking_msgs_INCLUDE_DIRS}
  ${${rviz_QT_VERSION}_INCLUDE_DIRS} ${spencer_human_attribute_msgs_INCLUDE_DIRS}
  ${Core_INCLUDE_DIRS} ${Widgets_INCLUDE_DIRS} ${Qt4_INCLUDE_DIRS}
  ${REQUIRED_INCLUDE_DIRS} ${QtGui_INCLUDE_DIRS} ${rviz_INCLUDE_DIRS}
  ${pedsim_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES}
  ${spencer_social_relation_msgs_LIBRARIES} ${EXACT_LIBRARIES} ${QtCore_LIBRARIES}
  ${Qt5_LIBRARIES} ${spencer_tracking_msgs_LIBRARIES}
  ${${rviz_QT_VERSION}_LIBRARIES} ${spencer_human_attribute_msgs_LIBRARIES}
  ${Core_LIBRARIES} ${Widgets_LIBRARIES} ${Qt4_LIBRARIES} ${REQUIRED_LIBRARIES}
  ${QtGui_LIBRARIES} ${rviz_LIBRARIES} ${pedsim_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES} ${spencer_social_relation_msgs_LIBRARIES}
  ${EXACT_LIBRARIES} ${QtCore_LIBRARIES} ${Qt5_LIBRARIES}
  ${spencer_tracking_msgs_LIBRARIES} ${${rviz_QT_VERSION}_LIBRARIES}
  ${spencer_human_attribute_msgs_LIBRARIES} ${Core_LIBRARIES} ${Widgets_LIBRARIES}
  ${Qt4_LIBRARIES} ${REQUIRED_LIBRARIES} ${QtGui_LIBRARIES} ${rviz_LIBRARIES}
  ${pedsim_LIBRARIES})
link_directories(${catkin_LIBRARY_DIRS})



## This plugin includes Qt widgets, so we must include Qt.
## We'll use the version that rviz used so they are compatible.
if(rviz_QT_VERSION VERSION_LESS "5")
  message(STATUS "Using Qt4 based on the rviz_QT_VERSION: ${rviz_QT_VERSION}")
  ## pull in all required include dirs, define QT_LIBRARIES, etc.
  include(${QT_USE_FILE})
  qt4_wrap_cpp(MOC_FILES src/detected_persons_display.h
    src/tracked_persons_display.h src/tracked_groups_display.h
    src/social_relations_display.h src/social_activities_display.h
    src/human_attributes_display.h src/person_display_common.h
    src/additional_topic_subscriber.h)
else()
  message(STATUS "Using Qt5 based on the rviz_QT_VERSION: ${rviz_QT_VERSION}")
  ## make target_link_libraries(${QT_LIBRARIES}) pull in all required dependencies
  set(QT_LIBRARIES Qt5::Widgets)
  qt5_wrap_cpp(MOC_FILES src/detected_persons_display.h
    src/tracked_persons_display.h src/tracked_groups_display.h
    src/social_relations_display.h src/social_activities_display.h
    src/human_attributes_display.h src/person_display_common.h
    src/additional_topic_subscriber.h)
endif()

add_definitions(-DQT_NO_KEYWORDS)



set(SOURCE_FILES src/detected_persons_display.cpp
  src/tracked_persons_display.cpp src/tracked_groups_display.cpp
  src/social_relations_display.cpp src/social_activities_display.cpp
  src/human_attributes_display.cpp src/person_display_common.cpp
  src/tracked_persons_cache.cpp src/visuals/person_visual.cpp ${MOC_FILES})


add_library(${PROJECT_NAME} ${SOURCE_FILES})
add_dependencies(${PROJECT_NAME} ${catkin_EXPORTED_TARGETS}) # for generation of message dependencies


install(TARGETS ${PROJECT_NAME}
  ARCHIVE
  DESTINATION lib
  LIBRARY
  DESTINATION lib
  RUNTIME
  DESTINATION bin)

install(FILES plugin_description.xml
  DESTINATION share/${PROJECT_NAME})

install(DIRECTORY media/ DESTINATION share/${PROJECT_NAME}/media)

install(DIRECTORY icons/ DESTINATION share/${PROJECT_NAME}/icons)

install(PROGRAMS scripts/send_test_msgs.py
  DESTINATION bin)

ament_export_dependencies(ament_cmake)
ament_export_dependencies(spencer_social_relation_msgs)
ament_export_dependencies(EXACT)
ament_export_dependencies(QtCore)
ament_export_dependencies(Qt5)
ament_export_dependencies(spencer_tracking_msgs)
ament_export_dependencies(${rviz_QT_VERSION})
ament_export_dependencies(spencer_human_attribute_msgs)
ament_export_dependencies(Core)
ament_export_dependencies(Widgets)
ament_export_dependencies(Qt4)
ament_export_dependencies(QtGui)
ament_export_dependencies(rviz)
ament_export_dependencies(pedsim)
ament_export_include_directories(${INCLUDE_DIRS})
ament_export_libraries(${PROJECT_NAME} ${LIBS})

ament_package()
