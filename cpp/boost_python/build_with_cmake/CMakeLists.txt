CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT(Python_Wrapper_Snippet)

#SET(CMAKE_CXX_COMPILER clang++)

# GET BOOST
FIND_PACKAGE(Boost COMPONENTS system thread python REQUIRED)
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS})
LINK_DIRECTORIES(${Boost_LIBRARY_DIRS})

# GET PYTHON
FIND_PACKAGE(PythonLibs REQUIRED)
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_DIRS})
LINK_DIRECTORIES(${PYTHON_LIBRARIES})

# BUILD LIB
SET(python_wrapper_src func.cc python_wrapper.cc)
ADD_LIBRARY(cppfunc SHARED ${python_wrapper_src})

# LINK LIBRARIES
TARGET_LINK_LIBRARIES(cppfunc ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

