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
    
    # hello function
    if hasattr(testlib,"hello"):
        call_hello_Ctypes = ctD.decoForCtypesCall(testlib.hello)
        call_hello_Ctypes()
    
        
    # fake function
    if hasattr(testlib,"pouet"):
        testlib.pouet()
    else :
        print("Pas de pouet")
            
    # moyenne_tableau function
    if hasattr(testlib,"moyenne_tableau"):
        
        testTabI = np.array([2, 2, 3, 3], dtype=np.intc) # np.intc equivaut au int de C mais np.int equivaut au long de C
        
        call_moyenne_tableau_Ctypes = ctD.decoForCtypesCall(testlib.moyenne_tableau)
        resMT = call_moyenne_tableau_Ctypes(args=[testTabI, testTabI.size], restype=ctD.dCtypes["double"])
        print("resMT = ", resMT)

        call_moyenne_tableau_double_Ctypes = ctD.decoForCtypesCall(testlib.moyenne_tableau_double)
        testTabD = np.array([2., 2.1, 3.5, 18.36], dtype=np.float64) # np.intc equivaut au int de C mais np.int equivaut au long de C
        
        resMT = call_moyenne_tableau_double_Ctypes(args=[testTabD, testTabD.size], restype=ctD.dCtypes["double"])
        print("resMT = ", resMT)
        
        # ajoute_entiers function
    if hasattr(testlib,"ajoute_entiers"):
        a = 48
        b = 42

        # call the decorator
        call_ajoute_entiers_Ctypes = ctD.decoForCtypesCall(testlib.ajoute_entiers)

        dict_args = {'args' : [a,b], 'restype' :  ctD.dCtypes["int"]}
        #dict_args = {'args' : [a,b]}
        res = call_ajoute_entiers_Ctypes(**dict_args)
        print("res = ", res)

        dict_args['args'] = [15, 53];
        
        res = call_ajoute_entiers_Ctypes(**dict_args)
        print("res = ", res)

        
    # fill_tableau function
    if hasattr(testlib,"fill_tableau"):
        # Initialize an array
        tabToFill = np.zeros((5,), dtype=np.intc) 

        # Call decorator
        call_fill_tableau_Ctypes = ctD.decoForCtypesCall(testlib.fill_tableau)

        # Execute fill_tableau with ctypes
        call_fill_tableau_Ctypes(args=[tabToFill, tabToFill.size])

        # Check results
        for ind in range(0,5):
            print("tab[ind] = ", tabToFill[ind])
            
