cmake_minimum_required(VERSION 3.15)
project(COP3530Proj3)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(COP3530Proj3
        Data.cpp
        Data.h
        Game.cpp
        Game.h
        main.cpp)
