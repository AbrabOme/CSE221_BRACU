# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l8hWPKm3tH_rrYw82iZM3rpkC6WCXk8Y
"""

task4_input = open(file='/content/drive/MyDrive/CSE221 lab2/input4.txt', mode='r')
task4_output = open(file='/content/drive/MyDrive/CSE221 lab2/output4.txt', mode='w')
num = int(task4_input.readline().strip())
f_lis = task4_input.readline().strip().split()

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

def merge(left,right):
    n = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[int(i)] >= right[int(j)]:
            n.append(int(left[i]))
            i += 1
            break
        else:
            n.append(int(right[j]))
            j += 1
            break
    return n
ans = mergeSort(f_lis)
task4_output.write(str(ans[0]))task4_input = open(file='/content/drive/MyDrive/CSE221 lab2/input4.txt', mode='r')
task4_output = open(file='/content/drive/MyDrive/CSE221 lab2/output4.txt', mode='w')
num = int(task4_input.readline().strip())
f_lis = task4_input.readline().strip().split()

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

def merge(left,right):
    n = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[int(i)] >= right[int(j)]:
            n.append(int(left[i]))
            i += 1
            break
        else:
            n.append(int(right[j]))
            j += 1
            break
    return n
ans = mergeSort(f_lis)
task4_output.write(str(ans[0]))