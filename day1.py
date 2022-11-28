"""
calculating the multiplication & sum of two  numbers && 
returning sum if product is less than 1000 else returning their product
"""
def sum_mul(x, y):
    sum = x + y
    mul = x * y
    if mul <= 1000:
        print("the sum is {}".format(sum))
    else:
        print("the product is {}".format(mul))

sum_mul(5, 40)
#finding the sum of the current number and previous number
#def sum_current_prev(current, prev):
prev = 0
    #determining the range of numbers
for x in range(0, 11):
        #calculating the sum
        sum = prev + x
        print("curent no: {}, previous no: {},the sum {}".format(x, prev, sum))
        prev = x
        
#printing characters from a string that are present at an even index number
word = input("enter word : ")
#using list slicicng
x = list(word)
for i in x[0::2]:
    print(i)
