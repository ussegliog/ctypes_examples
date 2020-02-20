#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>

extern "C"
{

  // Global variables (Just for example)  
  std::vector<int> vectInt; // Static => on stack
  std::vector<int> * vectIntPtr; // Dynamic => on heap with alloc/free
  std::vector<std::vector<double> *>  vect_vectDoublePtr; 
  std::vector<std::vector<double> >  vect_vectDouble;

  // Allocations
  void allocAndInitVectors()
  {
    // Just Init vectInt
    vectInt.push_back(42);
    vectInt.push_back(4242);

    // Just Init 
    std::vector<double> vecD0;
    vecD0.push_back(12);
    vecD0.push_back(1212);

    std::vector<double> vecD1;
    vecD1.push_back(13);
    vecD1.push_back(1313);

    vect_vectDouble.push_back(vecD0);
    vect_vectDouble.push_back(vecD1);
    
    // Alloc + Init
    vectIntPtr = new std::vector<int>();
    vectIntPtr->push_back(43);
    vectIntPtr->push_back(4343);

    std::vector<double> * vecPtrD0 = new std::vector<double>();
    vecPtrD0->push_back(22);
    vecPtrD0->push_back(2222);
    vecPtrD0->push_back(222222);
    std::vector<double> * vecPtrD1 = new std::vector<double>();
    vecPtrD1->push_back(23);
    vecPtrD1->push_back(2323);
    vecPtrD1->push_back(232323);

    vect_vectDoublePtr.push_back(vecPtrD0); 
    vect_vectDoublePtr.push_back(vecPtrD1);
  }

  // Free
  void freeVectors()
  {
    // Just clear
    vectInt.clear();

    // Clear + delete
    vectIntPtr->clear();
    delete vectIntPtr;
    vectIntPtr = 0;

    // Clear at each levels
    for (int i = 0; i < vect_vectDouble.size(); i++) 
      {
	vect_vectDouble[i].clear();
      }
    vect_vectDouble.clear();

    // Clear + delete at each levels
    for (int j = 0; j < vect_vectDoublePtr.size(); j++) 
      {
	vect_vectDoublePtr[j]->clear();
	delete vect_vectDoublePtr[j];
	vect_vectDoublePtr[j] = 0;
      }
    vect_vectDoublePtr.clear();
  }

  // Print
  void print_vect()
  {
    std::cout << "vectInt : " << std::endl;
    for (int i = 0; i < vectInt.size() ; i++) 
      {
	std::cout << vectInt[i] << std::endl;
      }


    std::cout << "vectIntPtr : " << std::endl;
    for (int i = 0; i < vectIntPtr->size() ; i++) 
      {
	std::cout << vectIntPtr->at(i) << std::endl;
      }

    std::cout << "vect_vectDouble : " << std::endl;
    for (int i = 0; i < vect_vectDouble.size() ; i++) 
      {
	for (int j = 0; j < vect_vectDouble[i].size(); j++) 
	  {
	    std::cout << vect_vectDouble[i].at(j) << std::endl;
	  }
      }

   std::cout << "vect_vectDoublePtr : " << std::endl;
   for (int i = 0; i < vect_vectDoublePtr.size() ; i++) 
      {
	for (int j = 0; j < vect_vectDoublePtr[i]->size(); j++) 
	  {
	    std::cout << vect_vectDoublePtr[i]->at(j) << std::endl;
	  }
      }
  }

  // Get Sizes
  int getVectIntSize()
  {
    return vectInt.size();
  }

  int getVectIntPtrSize()
  {
    return vectIntPtr->size();
  }
  
  void getVectVectDoubleShape(int * shape)
  {
    shape[0] = vect_vectDouble.size();
    if (shape > 0)
      shape[1] = vect_vectDouble[0].size();
  }

  void getVectVectDoublePtrShape(int * shape)
  {
    shape[0] = vect_vectDoublePtr.size();
    if (shape > 0)
      shape[1] = vect_vectDoublePtr[0]->size();
  }


  void fill_withVectVectDoublePtr(double * tabToFill, int sizeX, int sizeY)
  {
    // Check Size ...

    // Copy each value inside the vector into tabtoFill
    for (int i = 0; i < vect_vectDoublePtr.size() ; i++) 
      {
	for (int j = 0; j < vect_vectDoublePtr[i]->size(); j++) 
	  {
	    tabToFill[sizeY*i + j] = vect_vectDoublePtr[i]->at(j);
	  }
      }
  }

}
