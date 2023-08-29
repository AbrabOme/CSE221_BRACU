# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j5hfd4Um7SJaPlvgByZiUWGs0zFoHTyD
"""

#Task3

task3_input = open(file = 'input3.txt', mode='r')
task3_output = open(file = 'output3.txt', mode='w')
num = int(task3_input.readline().strip())
f_lis = task3_input.readline().strip().split()


def merge(left,right):
    n = []
    i = 0
    j = 0
    #print(left,right)
    while i < len(left) and j < len(right):
        if left[int(i)]<= right[int(j)]:
            n.append(int(left[i]))
            i += 1
        else:
            n.append(int(right[j]))
            j += 1


    while i < len(left):
        n.append(int(left[i]))
        i+=1

    while j < len(right):
        n.append(int(right[j]))
        j+=1


    return n

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        x = mergeSort(left)
        y = mergeSort(right)
    return merge(x,y)
answer=mergeSort(f_lis)
for i in range(len(answer)):
        task3_output.write(str(answer[i]) + " ")