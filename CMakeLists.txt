cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
project(COP3530Proj3)
## If you want to link SFML statically
# set(SFML_STATIC_LIBRARIES TRUE)
## In most cases better set in the CMake cache
# set(SFML_DIR "<sfml root prefix>/lib/cmake/SFML")

find_package(SFML 2.5 COMPONENTS graphics audio REQUIRED)
#add_executable(COP3530Proj3 main.cpp)
add_executable(COP3530Proj3 main.cpp Game.cpp Game.h Data.cpp Data.h)
target_link_libraries(COP3530Proj3 sfml-graphics sfml-audio)