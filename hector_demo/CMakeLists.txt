cmake_minimum_required(VERSION 3.0.2)
project(hector_demo)

find_package(catkin REQUIRED COMPONENTS
  # hector_mapping
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(FILES
  launch/from_bag.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
