#include <stdio.h>
#include <stdlib.h>
#include <iostream>

extern "C"
{  

  void hello()
  {
    std::cout << "Hello World " << std::endl;
    float sf = 2.1;
  }
  
  
  int ajoute_entiers(int a, int b)
  {
    int sum = a+b;
    a = 0;
    return sum;
  }
  
  double moyenne(double a, double b)
  {
    return (a + b)/2;
  }
     
  double moyenne_tableau(int * tab, int n)
  {
        int i=0;
        double s = 0;
        for (i=0; i<n; i++){
	  s += tab[i];
	  tab[i] = 0;
        }

	double res = s/n;
	
        return res;
  }

  
  double moyenne_tableau_float(float * tab, int n)
  {
        int i=0;
        double s = 0;
        for (i=0; i<n; i++){
	  s += tab[i];
	  tab[i] = 0;
        }

	double res = s/n;
	
        return res;
  }

  double moyenne_tableau_double(double * tab, int n)
  {
        int i=0;
        double s = 0;
        for (i=0; i<n; i++){
	  s += tab[i];
	  tab[i] = 0;
        }

	double res = s/n;
	
        return res;
  }

  
  void fill_tableau(int * tab, int n)
  {
    for (int i=0; i<n; i++)
      {
	tab[i] = 42+i;
      }

  }
  
}
