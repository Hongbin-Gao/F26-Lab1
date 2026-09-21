
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date:2026/09/18
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.

quantity = 1.23
stock = float(input(("Enter a decimal number: ")))
print("The product is %4.2f" %(quantity * stock))
print("The product is %7.2f" %(quantity * stock))