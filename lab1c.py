
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/09/18
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'

import math
radius = int(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
print("Area of the circle is", area_of_circle)