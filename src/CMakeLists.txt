cmake_minimum_required(VERSION 3.10)
project(CI_CD_Project)

set(CMAKE_CXX_STANDARD 14)

add_executable(main app/main.cpp app/utils.cpp)
add_executable(test_main tests/test_main.cpp app/utils.cpp)
