PROJECT(LIB_TEST_CPP)

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

IF(COMMAND CMAKE_POLICY)
  CMAKE_POLICY(SET CMP0003 NEW)
ENDIF(COMMAND CMAKE_POLICY)


SET(CMAKE_MODULE_PATH
   ${CMAKE_SOURCE_DIR}/CMake)

#-----------------------------------------------------------------------------
# Test for some required system information.
INCLUDE (${CMAKE_ROOT}/Modules/CMakeBackwardCompatibilityC.cmake)
INCLUDE (${CMAKE_ROOT}/Modules/CMakeBackwardCompatibilityCXX.cmake)

# Set the Buildname for the dashboard
SET(BUILDNAME "${BUILDNAME}" CACHE STRING "Name of build on the dashboard")

#-----------------------------------------------------------------------------
# Compilation options


SET(CMAKE_C_FLAGS " -O2")
SET(CMAKE_CXX_FLAGS " -O2")

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}"  CACHE STRING "Flag used for openMP." FORCE)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}"  CACHE STRING "Flag used for openMP." FORCE)


# Include directories
INCLUDE_DIRECTORIES(
${LIB_TEST_CPP_BINARY_DIR} 
${LIB_TEST_CPP_INCLUDE_DIRS})

INCLUDE_DIRECTORIES(${LIB_TEST_CPP_SOURCE_DIR})

#-----------------------------------------------------------------------------
# Libraries Stela_medee.a
FILE(GLOB BIB_TEST_FOR_CTYPES_CPP "${LIB_TEST_CPP_SOURCE_DIR}/files_cpp/*.cpp")

set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

ADD_LIBRARY(BIB_Test_CPP SHARED  ${BIB_TEST_FOR_CTYPES_CPP})
