# Given  sets of integers, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
M = (input('enter your number with space after each'))
# change the integers into set
set_M = set(map(int, M.split()))
N = (input('enter your number with space after each'))
set_N = set(map(int, N.split()))

# finding the symmetry difference

symmetric_diff = sorted(set_M.symmetric_difference(set_N))
for num in symmetric_diff:
    print(num)

# print(num)

