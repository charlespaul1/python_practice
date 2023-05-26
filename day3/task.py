# given the participants's score sheet for your university sports day, 
# you are required to find the runner up score. you are given n scores. 
# store them in a list and find the score of the runner up. 
# input format is the first line contains n 
# . the second line contains an array A[] of n integers 
# each separated by a space. using python print the runner-up score
n = input('input n:')
arr= map(int, input('in put scores:').split())
#  storing the scores in a list
sorted_scores = sorted(set(arr), reverse = True)
runner_up = sorted_scores[1]
print('the runner up is: ',runner_up)
        