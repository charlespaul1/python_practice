# def add(a, b):
#     return a + b

# def Subtraction(a, b):
#     return a - b

# def Multiplication(a, b):
#     return a * b

# def Division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print('Error: Cannot divide by zero')


# def Exponention(a, b):
#     return a ** b

# print('Select your operation')
# print('1. Add')
# print('2. Subtraction')
# print('3. Multiplication')
# print('4. Division')
# print('5. Exponention')


# while True:
#     choice = input('enter your choice (1 - 4): ')
    
#     if choice in ['1', '2', '3', '4', '5']:
#         num1 = float(input('Enter first number: '))
#         num2 = float(input('Enter second number: '))
        
#         if choice == '1':
#             print('Result', add(num1, num2))
#         if choice == '2':
#             print('Result', Subtraction(num1, num2))
#         if choice == '3':
#             print('Result', Multiplication(num1, num2))
#         if choice == '4':
#             print('Result', Division(num1, num2))
#         if choice == '5':
#             print('Result', Exponention(num1, num2))
            
#         break
#     else:
#         print('Invalid Input')
    
    



def  add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a , b):
    if b != 0:
        return a / b
    else:
        print('Error: Division by 0 ')
        

print('Pick a sign')
print('1. add')
print('2. subtraction')
print('3. division')
print('4. multiplication')
while True:
    choice = input('select your sign: ')
    if choice in ['1', '2','3','4']:
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter the second number: '))
        
        if choice == '1':
            print('Result', add(num1, num2))
        if choice == '2':
            print('Result', subtraction(num1, num2))
        if choice == '3':
            print('Result', Division(num1, num2))
        if choice == '4':
            print('Result', Multiplication(num1, num2))
        break
    else:
        print('Invalid input')

    
    
    
    
    
    