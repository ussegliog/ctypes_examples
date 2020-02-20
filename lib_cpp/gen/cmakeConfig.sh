#!/bin/sh

path_begin="$(pwd)"
path="$(dirname $0)"


# Create build repository
if [ -d "${path}/build" ]
then
    echo "build exist"
    rm -rf ${path}/build
fi

mkdir ${path}/build

cd ${path}/build

cmake -DCMAKE_CXX_COMPILER=g++ ../../src

cd ${path_begin}
