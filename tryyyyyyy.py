# Define a global variable
global  global_var 

# Function that modifies the global variable
def modify_global_variable():
    global global_var  # Declare the global variable
    global_var = 20    # Modify the global variable

# Print the global variable before and after calling the function
print("Before:", global_var)
modify_global_variable()
print("After:", global_var)
