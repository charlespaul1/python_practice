# list comprehension
# syntax: [expression for item in iterable if condition == True]
# the return value is a new list leaving the old list unchanged
# with no if condition the syntax is [expression for item in iterable]
# the iterable can be a list, tuple, set, dictionary, string
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [fruit for fruit in fruits if "w" in fruit]

print(newList)
# using python list comprehension  solve this and explain 
# it step by step. you are given 3 integers x, y and z 
# representing the dimensions of a cuboid along with an integer n. 
# print all possible coordinates given by (i, j,k) on  3D grid where 
# the sum of i + j + k is not equal to n. Here 0<= i <= x; 0 <= j <= y; 
# 0<=k  <=z. print an array of elements that do not sum to n = 3, 
# Print the list in lexicographic increasing order.


# getting the dimensions of the cuboid on all axis
x = 1
y = 1
z = 1
n = 2
# list comprehension to get the coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if(i + j + k ) != n]
# sorting the coordinates in a lexicographic increasing order
sorted_coordinates = sorted(coordinates)

# printing the coordinates
for coordinate in sorted_coordinates:
    print(coordinate)
