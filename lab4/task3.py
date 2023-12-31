# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YOX1foph-bIaD589yPv4grsutqV2wkeZ
"""

task3_input = open(file='input3.txt', mode='r')
task3_output = open(file='output3.txt', mode='w')

lst = task3_input.readline().strip().split(" ")
v = int(lst[0])
e = int(lst[1])
visited = [False]*(v+1)
adj_list = {}
for i in range(1,v+1):
    adj_list[i] = []

for i in range(e):
    lst2 = task3_input.readline().strip().split()
    u = int(lst2[0])
    v = int(lst2[1])
    adj_list[u].append(v)
    adj_list[v].append(u)



def DFS (adj_list,st):
    visited[st] = True
    task3_output.write(str(st)+ " ")
    for i in adj_list[st]:

        if visited[i]==False:
            visited[i]=True
            DFS(adj_list, i)
DFS(adj_list,1)