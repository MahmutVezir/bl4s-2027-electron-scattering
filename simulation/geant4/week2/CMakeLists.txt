cmake_minimum_required(VERSION 3.16)
project(BL4SWeek2SensitiveTracker LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Geant4 11.4 REQUIRED)
include(${Geant4_USE_FILE})

file(GLOB_RECURSE WEEK2_SOURCES CONFIGURE_DEPENDS
    ${PROJECT_SOURCE_DIR}/src/*.cc
)

add_executable(week2_tracker ${WEEK2_SOURCES})
target_include_directories(week2_tracker PRIVATE
    ${PROJECT_SOURCE_DIR}/include
    ${Geant4_INCLUDE_DIRS}
)
target_link_libraries(week2_tracker PRIVATE ${Geant4_LIBRARIES})

message(STATUS "Geant4 version: ${Geant4_VERSION}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
