limit = 100

for num in range(1, limit + 1):
    # check divisibility by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("fizz buzz")
        # check divisible by 3
    elif num % 3 == 0 :
        print('Fizz')
        # check divisible by 5
    elif num % 5 == 0:
        print( 'Buzz')
    else:
        print(num)
        