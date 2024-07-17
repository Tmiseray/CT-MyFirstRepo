# Declare a variable and assign a value
a = 13

# Print value type
print("The type of value for a is: ", type(a))

# Reassign different type of value for same variable
a = "Alpha"

# Print new value type
print("The new type of value for a is: ", type(a))

# Assign values to multiple variables in one line
# Multi-Variable Reference: https://www.geeksforgeeks.org/assigning-multiple-variables-in-one-line-in-python/#
# Variable Naming Convention Reference: https://www.w3schools.com/python/python_variables_names.asp
a, varB, Var_C = "Alpha", 13, "Charlie"

# Print values for each variable
print("The value of a is: ", a)
print("The value of varB is: ", varB)
print("The value of Var_C is: ", Var_C)