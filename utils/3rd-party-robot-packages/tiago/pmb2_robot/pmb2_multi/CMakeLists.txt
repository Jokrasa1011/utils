cmake_minimum_required(VERSION 3.5)
project(pmb2_multi)
find_package(catkin REQUIRED COMPONENTS)
catkin_package()

install(
  PROGRAMS
    scripts/pose_writing.sh
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

foreach(dir config launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach()

