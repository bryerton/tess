cmake_minimum_required(VERSION 3.10)

project(tess_test)

add_executable(tess_test main.c)

target_link_libraries(tess_test zmq)