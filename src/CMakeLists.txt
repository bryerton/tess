cmake_minimum_required(VERSION 3.10)

project(tess)

add_library(tess tess_zeromq.c)

target_link_libraries(tess zmq)

