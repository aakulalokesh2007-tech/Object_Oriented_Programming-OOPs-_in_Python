Checking Instances
=====================================

This repository contains a simple Python script demonstrating how to use the built-in `isinstance()` function to check an object's type in Object-Oriented Programming (OOP).

Description
-----------
The script defines two unrelated classes, `he` and `hr`, and creates one instance of each. It then uses a series of `isinstance()` checks to verify whether a specific object belongs to a specific class. This function is incredibly useful in larger applications for type-checking and ensuring that variables hold the expected objects before executing class-specific methods.

Code Overview
-------------
- class he: A basic class containing a placeholder method `no()`.
- class hr: A basic class containing a placeholder method `show()`.
- a = he(): Instantiates an object of class `he`.
- b = hr(): Instantiates an object of class `hr`.
- isinstance(object, class): The built-in function used to check if the first argument (object) is an instance of the second argument (class).

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
When you run the script, it prints the boolean result of each type check. 

Output:
False
True
True
False

Notes
-----
The `pass` keyword is used inside the class methods as a placeholder. It tells Python to do nothing, allowing the classes to be defined syntactically correctly without needing to implement actual logic inside the methods right away.
