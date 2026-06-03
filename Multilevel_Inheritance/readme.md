Multilevel Inheritance
=========================================

This repository contains a simple Python script demonstrating the concept of multilevel inheritance in Object-Oriented Programming (OOP).

Description
-----------
The script defines three classes (`a`, `c`, and `b`) structured in a multilevel hierarchy. Class `c` inherits from class `a`, and class `b` inherits from class `c`. This demonstrates how a derived class inherits features not just from its immediate parent, but from all ancestors in the inheritance chain.

Continuing the theme of previous scripts, this code uses `me` instead of the standard `self` convention for instance methods.

Code Overview
-------------
- class a: The base (grandparent) class with method `ass()`.
- class c(a): The intermediate (parent) class with method `bi()`. Inherits from `a`.
- class b(c): The derived (child) class with method `re()`. Inherits from `c` (and consequently, from `a`).
- A = b(): Instantiates the lowest-level class.

Getting Started
---------------
Prerequisites:
- Python 3.x installed on your machine.

How to Run:
1. Clone this repository or download the source code file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
   python your_script_name.py

Example Output
--------------
When you run the script, the single instance of class `b` successfully calls methods from all three levels of the inheritance hierarchy:

in a
in c
in b

Notes
-----
Multilevel inheritance is a powerful feature that allows for deep hierarchical classifications, but it should be used carefully in large projects to avoid overly complex dependencies.
