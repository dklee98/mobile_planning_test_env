cmake_minimum_required(VERSION 3.0.2)
project(mobile_planning_test_env)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  laser_geometry
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})
include_directories(${EIGEN3_INCLUDE_DIRS} ${DECOMP_UTIL_INCLUDE_DIRS})

catkin_install_python(PROGRAMS
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# add_executable(collision_free_node src/collision_free.cpp)
# target_link_libraries(collision_free_node ${catkin_LIBRARIES} ${EIGEN3_LIBS} ${OpenCV_LIBS})
