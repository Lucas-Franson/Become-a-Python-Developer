#
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# Re-declaring the variables works
f="abc"
print(f)

# Error: variables of different types cannot be combined
print('this is a string ' + 123)

# Global vs. Local local variables in function
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

del f 
print(f)
