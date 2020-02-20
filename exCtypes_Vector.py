#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import numpy as np

from srcPy import CtypesDecorator as ctD


########################## Main ##########################"
if __name__ == "__main__":
    # Get file's directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Load Library
    testlib = ctD.loadLibrary("./lib_cpp/gen/build/lib/libBIB_Test_CPP.so")
    
    # allocAndInitVectors function
    if hasattr(testlib,"allocAndInitVectors"):
        call_allocAndInitVectors_Ctypes = ctD.decoForCtypesCall(testlib.allocAndInitVectors)
        call_allocAndInitVectors_Ctypes()
    

    # print_vect function
    if hasattr(testlib,"print_vect"):
        call_printVectors_Ctypes = ctD.decoForCtypesCall(testlib.print_vect)
        call_printVectors_Ctypes()
        
       
    # Get sizes
    # Initialize arrays
    shape1 = np.zeros((2,), dtype=np.intc) 
    shape2 = np.zeros((2,), dtype=np.intc) 

    # Vect1 = vectInt
    # Vect2 = vectIntPtr
    # Vect3 = vectVectDouble
    # Vect4 = vectVectDoublePtr
    call_getVectIntSize_Ctypes = ctD.decoForCtypesCall(testlib.getVectIntSize)
    sizeVect1 = call_getVectIntSize_Ctypes(restype=ctD.dCtypes["int"])
    print("sizeVect1 = ", sizeVect1)

    call_getVectIntPtrSize_Ctypes = ctD.decoForCtypesCall(testlib.getVectIntPtrSize)
    sizeVect2 = call_getVectIntPtrSize_Ctypes(restype=ctD.dCtypes["int"])
    print("sizeVect2 = ", sizeVect2)

    call_getVectVectDoubleShape_Ctypes = ctD.decoForCtypesCall(testlib.getVectVectDoubleShape)
    call_getVectVectDoubleShape_Ctypes(args=[shape1])
    print("shape1 = ", shape1)

    call_getVectVectDoublePtrShape_Ctypes = ctD.decoForCtypesCall(testlib.getVectVectDoublePtrShape)
    call_getVectVectDoublePtrShape_Ctypes(args=[shape2])
    print("shape2 = ", shape2)


    tabVect = np.zeros((shape2[0], shape2[1]), dtype=np.float64)
    call_fill_withVectVectDoublePtr_Ctypes = ctD.decoForCtypesCall(testlib.fill_withVectVectDoublePtr)
    call_fill_withVectVectDoublePtr_Ctypes(args=[tabVect, int(shape2[0]), int(shape2[1])])
    print(tabVect)


    # freeVectors function
    if hasattr(testlib,"freeVectors"):
        call_freeVectors_Ctypes = ctD.decoForCtypesCall(testlib.freeVectors)
        call_freeVectors_Ctypes()
