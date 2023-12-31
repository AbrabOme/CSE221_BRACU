# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iDq-XTyJ-Chu-ZpCimAl4lCTG2_7IgVw
"""

#Task 3
task3_input = open(input3.txt', mode='r')
task3_output = open(output3.txt', mode='w')

num_of_line = int(task3_input.readline())
id = task3_input.readline().strip().split()
for i in range(len(id)):
    id[i] = int(id[i])

marks = task3_input.readline().strip().split()
for i in range(len(marks)):
    marks[i] = int(marks[i])

for i in range(len(marks)):
    maxi = i
    for j in range(i+1,len(marks)):
        if marks[maxi] < marks[j]:
            maxi = j
        marks[maxi],marks[i] = marks[i],marks[maxi]
        id[maxi], id[i] = id[i], id[maxi]

dic = {}
for i in range(len(marks)):
    if marks[i] not in dic:
        dic[marks[i]] = [id[i]]
    else:
        dic[marks[i]].append(id[i])

for i,j in dic.items():
    if len(j) == 1:
        task3_output.write(f"ID: {str(j[0])} Mark: {str(i)}\n")

    else:
        for x in range (len(j)):
            y = min(j)
            task3_output.write(f"ID: {str(y)} Mark: {str(i)}\n")
            j.remove(y)