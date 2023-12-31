# -*- coding: utf-8 -*-
"""Task1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YOX1foph-bIaD589yPv4grsutqV2wkeZ
"""

task1a_input = open(file='input1a.txt', mode='r')
task1a_output = open(file='output1a.txt', mode='w')
lst = task1a_input.readline().strip().split(" ")
v = int(lst[0])
e = int(lst[1])

adj_mat = [[0 for _ in range(v+1)] for _ in range(v+1)]

for i in range(e):
    lst2 = task1a_input.readline().strip().split()
    u = int(lst2[0])
    v = int(lst2[1])
    w = int(lst2[2])
    adj_mat[u][v] = w

task1a_input.close()

for row in adj_mat:
    elem_row = ""
    for element in row:
        # print(element, end=' ')
        elem_row = elem_row + " " + str(element)
    # print()
    elem_row = elem_row + "\n"
    task1a_output.write(elem_row)

task1a_output.close()