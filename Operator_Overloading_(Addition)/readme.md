Operator Overloading (Addition)
==================================================

This repository contains a simple Python script demonstrating how to overload the mathematical addition operator (`+`) in Object-Oriented Programming (OOP) using the `__add__` magic method.

Description
-----------
The script defines a `demo` class that encapsulates a single numeric value (`x`). By defining the `__add__` special double-underscore (dunder) method, we instruct Python on exactly how to behave when it encounters the `+` symbol between two instances of the `demo` class. 

Instead of throwing a TypeError, the custom method adds the internal `x` values of both objects and returns the resulting integer. This script continues the exploration of positional instance arguments by using `me` instead of `self`.

Code Overview
-------------
- class demo: The main class definition.
- __init__(me, x): Constructor that initializes the object's internal value `me.x` with the passed argument `x`.
- __add__(me, y): Overloads the `+` operator. The `me` parameter represents the object on the left side of the `+`, while `y` represents the object on the right side. It returns the sum of `me.x` and `y.x`.

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
In the provided example, instances are created and added together:
a = demo(20)
b = demo(30)
d = (a + b)  # Results in 50

The script then demonstrates creating temporary instances inline to add the result (`d`) to a new value:
demo(d) + demo(10)  # Results in 60

Output:
50
60

Notes
-----
Notice that the `__add__` method in this specific implementation returns a standard integer, not a new instance of the `demo` class. Depending on your program's needs, you could modify `__add__` to return a new class instance instead (e.g., `return demo(me.x + y.x)`).
