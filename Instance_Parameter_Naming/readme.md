## Instance Parameter Naming
============================================

This repository contains a simple Python script demonstrating how Python handles instance references in Object-Oriented Programming (OOP). 

## Description
-----------
The script defines a `Person` class to store a name and an age. The key takeaway from this script is that Python does not strictly enforce the use of the `self` keyword for instance methods. 

By creatively using `yes` in the constructor and `abc` in the instance method, this code proves that Python tracks the instance based purely on the parameter's position (the first argument) rather than a reserved keyword.

## Code Overview
-------------
- class Person: The main class definition.
- __init__(yes, name, age): Constructor using 'yes' instead of 'self' to initialize the name and age attributes.
- myfunc(abc): A method using 'abc' instead of 'self' to access attributes and print a greeting.

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

# Example Output
--------------
When you run the script, it creates a Person instance for "John" who is 36, and outputs:

Hello my name is Johnmy age is  36

Notes
-----
While this is a great educational experiment to understand positional arguments in classes, standard Python convention highly recommends sticking to `self` in production code for better readability and collaboration.
