#!/usr/bin/env python
# coding: utf-8

# # Grade Calculator

# In[1]:


score = float(input("Please, enter your score: "))

if score <= 0:
    print('ERROR: enter a valid number!')
else:
    total_points = float(input("Please, enter the total points: "))

    grade = round(score / total_points * 100.0, 2)

    output = "Your grade: " + str(grade) + "%"

    print(output)

    print('Letter Grade: ')

    if grade <= 100 and grade >= 89.5: 
        print('A')
    elif grade <= 89.5 and grade >= 79.5: 
        print('B')
    elif grade < 79.5 and grade >= 69.5: 
        print('C')
    elif grade < 69.5 and grade >= 59.5: 
        print('D')
    elif grade < 59.5 and grade >= 0: 
        print('Fail')
    else:
        print('ERROR: enter a valid score!')

