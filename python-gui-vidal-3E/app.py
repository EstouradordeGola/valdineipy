# Arrays (we'll use the numpy library)
import numpy as np 

#create an array 
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

#acessing elements
print("First element:", array [0])
print("Last element:", array [-1])

# Slicing
print("ELements from 1 to 3", array[1:3])

# Lists
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

#append an element
my_list.append(6)
print("List after append:", my_list)

# Insert an element at a specific position
my_list.insert(2, 7)
print("List after insert:", my_list)

# Remove an element
my_list.remove(4)
print("List after remove:", my_list)

#Tuples 
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

#acessing elements (same as lists)
print("First element:", my_tuple [0])
print("Last element:", my_tuple [-1])

#lamps
#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while loop
    i = 0
    while i < 5:
        print(i)
        i += 1

#looping over a list with indices

my_list = [1, 2, 3, 4, 5]
for i, element in enumerate(my_list):
    print(f"index {i}: {element}")