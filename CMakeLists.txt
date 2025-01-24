cmake_minimum_required(VERSION 2.6)

set(PROJECT_NAME example)

project(${PROJECT_NAME} CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

aux_source_directory(. SRC_FILES)

add_executable(${PROJECT_NAME} ${SRC_FILES})