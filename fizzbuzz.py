limit = 100

for num in range(1, limit + 1):
    # divisible by 3 and 5
    if num % 3 == 0 and  num % 5 == 0:
        print('fizz buzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)