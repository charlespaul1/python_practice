# reading number of commands from user so as to know how many operations are to be perfomed to the list
N = int(input('enter number of commands:'))
# initializing an empty list that will store elements that we manipulate usiing the commands
the_list = []
# a loop that will run for N times
for _ in range(N):
    # reading command from user
    command = input('enter command: ').split()
    # check the first word in the command to determine the operation
    if command[0] == 'insert':
        index = int(command[1])
        value = int(command[2])
        the_list.insert(index, value)
    elif command[0] == 'print':
        print(the_list)
    elif command[0] == 'remove':
        the_list.remove(int(command[1]))
    elif command[0] == 'append':
        value = int(command[1])
        the_list.append(value)
    elif command[0] == 'sort':
        the_list.sort()
    elif command[0] == 'pop':
        the_list.pop()
    elif command[0] == 'reverse':
        the_list.reverse()
    else:
        print('invalid command')
        

