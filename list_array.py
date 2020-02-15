# Python3 code to demonstrate working of 
# Convert list to Python array 
# Using array() + data type indicator 
from array import array 

# initializing list 
test_list = [6, 4, 8, 9, 10] 

# printing list 
print("The original list : " + str(test_list)) 

# Convert list to Python array 
# Using array() + data type indicator 
res = array("i", test_list) 

# Printing result 
print("List after conversion to array : " + str(res)) 
