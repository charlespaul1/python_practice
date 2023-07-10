# getting number of elements in a tuple
n = int(input("Enter the number of elements in the tuple: "))
integer_list = map(int, input("Enter the elements of the tuple: ").split())
t = tuple(integer_list)
result = hash(t)
print(result)