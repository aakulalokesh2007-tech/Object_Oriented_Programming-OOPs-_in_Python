## Magic Methods


This repository contains a simple Python script demonstrating how to overload comparison operators in Object-Oriented Programming (OOP) using Python's "magic" (dunder) methods.

## Description

The script defines a `com` class that implements custom logic for standard mathematical comparisons (like less than, greater than, etc.). By defining these special double-underscore methods, instances of this class can be compared directly using standard Python operators (e.g., `<`, `<=`). 

Additionally, this code continues the experiment of using non-standard parameter names (`me` instead of `self`, and `ot` instead of `other`) to demonstrate how Python relies on argument position.

## Code Overview

- class com: The main class definition.
- __init__(me, x): (Implied) Constructor to initialize the value `x`.
- __lt__(me, ot): Overloads the `<` (less than) operator.
- __le__(me, ot): Overloads the `<=` (less than or equal to) operator.
- __gt__(me, ot): Overloads the `>` (greater than) operator.
- __ge__(me, ot): Overloads the `>=` (greater than or equal to) operator.

## Getting Started

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

## Example Output

In the provided example, two instances are created: `a = com(20)` and `b = com(2)`. 
When the script evaluates `c = (a <= b)`, it triggers the custom `__le__` method, checking if 20 is less than or equal to 2.

## Output:
False

## Notes
-----
Note: The provided snippet assumes an `__init__` method exists to assign the passed integer to `me.x`. If running this code from scratch, ensure you include the `__init__` method to avoid an AttributeError!
