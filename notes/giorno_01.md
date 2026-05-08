### 1. Python interpreter
- An interpreter is what runs a python code. 
-  It first converts the code to the AST(Abstract syntax tree) which is then compiled to bytecode by python. Now, the PVM(python virtual machine) reads the bytecode and executes it line by line

### 2. Virtual environments
- Virtual env is a isolated python environment with its own interepreter, packages and dependencies
- To create ```python -m  venv venv ```
- To activate ```source venv/bin/activate```
- To deactivate ```deactivate```


### 3. What is requirements.txt
- Its a file to list all external dependencies and also can be used to fix the deps. 
- To install everything from req.txt ```pip install -r requirements.txt```
- To freeze ```pip freeze > requirements.txt ```

### 4. Python objects
- In Python, everything is an object-number,string,functions. Object have an entity, type and value. Objects are created in heap.

### 4. Variables
- a variable in python is NOT a container to store values. Rather a name that reference an object
- variables point to object
- No type declaration like java or js

### 5. Tuples
- Collection of different data types
- ordered and unchangable(immutable)
- once created cannot change the values
- we have : tuple(), count(), index(), + 

### 6. Sets
- set is a collection of items. store multiple items in one variable 
- unordered, unchangable , no dublicate allowed