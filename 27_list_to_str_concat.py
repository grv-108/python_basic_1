# 27. List to String Concatenator

# Write a Python program that concatenates all elements in a list into a string and returns it.

my_list = [1, 'hi', 2.3, 'nice', 'world', 'python']

my_str = ""
for x in my_list:
    my_str += " "+str(x)
    
print(my_str)