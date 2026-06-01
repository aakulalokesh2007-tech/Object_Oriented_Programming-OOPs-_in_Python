## Private Variables
====================================================

This repository contains a simple Python script demonstrating how Python handles name mangling to simulate private variables in Object-Oriented Programming (OOP).

##  Description
-----------
The script defines a `var` class with a public attribute `na` and a "private" attribute `__num`. In Python, prefixing an attribute with double underscores (`__`) invokes name mangling. This changes the way the attribute is accessed from outside the class to prevent accidental modification or overriding.

## Code Overview
-------------
- class var: The main class definition.
- go(self): A method that initializes a public attribute `self.na` and a mangled attribute `self.__num`.
- no(self): A method that prints both attributes from within the class.

## Getting Started
---------------
Prerequisites:
- Python 3.x installed on your machine.
```
How to Run:
1. Clone this repository or download the source code file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
   python your_script_name.py
```

Example Output
--------------
When you run the script, it demonstrates accessing the variables both internally (via a method) and externally (via the mangled name):

name= lok
number 110112
110112

Notes
-----
The final print statement `print(p._var__num)` successfully accesses the "private" variable from outside the class by using its mangled name (`_ClassName__VariableName`). This proves that Python's private variables are not strictly private, but rather renamed to prevent accidental access.
