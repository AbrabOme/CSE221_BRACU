# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18VIT-kRKrafjoCOUimUq6ydJoLSJSm82
"""

#Task2

task2_input = open(file='input2.txt', mode='r')
task2_output = open(file='output2.txt', mode='w')
high = 0

num = int(task2_input.readline().strip())
f_lis = task2_input.readline().strip().split()

arr = []
for i in f_lis:
    arr.append(int(i))


def merge(left,right):
    n = []
    i = 0
    j = 0


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
        comp_sum(0)
        return arr

    elif len(arr) == 2:
        comp_sum(int(arr[0])+int(arr[1])**2)
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        x = mergeSort(left)
        y = mergeSort(right)
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        left_max = max(left)
        right_max = 0
        for i in right:
            r = (int(i))**2
            if r > right_max:
                right_max = r
        comp_sum(left_max + right_max)


        x = mergeSort(left)
        y = mergeSort(right)

    return merge(x,y)


def comp_sum(sum):
    global high
    if int(sum) > high:
        high = int(sum)

    else:
        pass
    return high


answer=mergeSort(arr)
x = comp_sum(high)

task2_output.write(str(x))