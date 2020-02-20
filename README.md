# ctypes_examples

Two kinds of examples with 
* exCtypes : call functions defined into Hello.cpp
* exCtypes_Vector : call functions defined into Vectors.cpp


To test ctypes examples :
* Compile lib_cpp to obtain **libBIB_Test_CPP.so** by :
  * Launching ./cmakeConfig.sh (into lib_cpp/gen/)
  * Going to build directory and executing make command
* Launch exCtypes.py or exCtypes_Vector.py

A decorator defined into CtypesDecorator.py encapsulates the ctypes calls from Python and defined the main types.
