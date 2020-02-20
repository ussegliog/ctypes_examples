#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes
import sys
import os
import numpy as np
import inspect


########################## Dictionary for ctypes and basics types matching ##########################
dCtypes = {'double': ctypes.c_double, 'int' : ctypes.c_int }


########################## Load Library ##########################
def loadLibrary(pathToLibrary):
    lib = None
    
    if not os.path.isfile(pathToLibrary) :
        print("Library does not exist")
    else :
        lib = ctypes.cdll.LoadLibrary(pathToLibrary)
        
    return lib


########################## Full the argtypes list ##########################
def fullArgtypes(listArgs, listArgTypes):

    # Fill listArgs accordings to args        
    for arg in listArgs:

        # Basics types
        if isinstance(arg, int):
            
            listArgTypes.append(ctypes.c_int)
        if isinstance(arg, bool):
            listArgTypes.append(ctypes.c_bool)
        if isinstance(arg, float):
            listArgTypes.append(ctypes.c_double)

        # Numpy Array
        if isinstance(arg, np.ndarray ) :
            if arg.dtype == np.intc :
                listArgTypes.append(np.ctypeslib.ndpointer(ctypes.c_int, ndim=arg.ndim, flags="C_CONTIGUOUS"))
            if arg.dtype == np.float32 :
                listArgTypes.append(np.ctypeslib.ndpointer(ctypes.c_float, ndim=arg.ndim, flags="C_CONTIGUOUS"))
            if arg.dtype == np.float64 :
                listArgTypes.append(np.ctypeslib.ndpointer(ctypes.c_double, ndim=arg.ndim, flags="C_CONTIGUOUS"))
            


########################## Decorator for CTypes Function ##########################"
def decoForCtypesCall(cFunc):
    """ Decorator for ctypes call (c++ function) """

    def wrapper(**kwargs):
        
        # Init my lists 
        listArgs = []
        listArgTypes = []
        restype = None
        
        for key, value in kwargs.items():
            # Get elts into **kwargs dictionary (2 possible elts : args and restype) 
            if key == "args" or key == "restype" :
                if key == "args":
                    listArgs = value
                elif key == "restype":
                    restype = value
            else :
                print("Expected keys not existed for decoForCtypesCall")
                return 0

        # Fill lists
        fullArgtypes(listArgs, listArgTypes)

        # Ctypes arg and res types
        cFunc.argtypes = listArgTypes
        cFunc.restype = restype

        # Execute cFunc
        resAjout = cFunc(*listArgs)

        # Return the result
        return resAjout
        
    # Return the wrapper function
    return wrapper


