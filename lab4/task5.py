# -*- coding: utf-8 -*-
"""Task5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YOX1foph-bIaD589yPv4grsutqV2wkeZ
"""

task5_input = open(file='input5.txt', mode='r')
task5_output = open(file='output5.txt', mode='w')

lst = task5_input.readline().strip().split(" ")
v = int(lst[0])
e = int(lst[1])
need = int(lst[2])
parent_list = {}
adj_list = {}
for i in range(1,v+1):
    adj_list[i] = []
    parent_list[i] = None
for i in range(e):
    lst2 = task5_input.readline().strip().split()
    u = int(lst2[0])
    v = int(lst2[1])
    adj_list[u].append(v)
    adj_list[v].append(u)
queue = []

def bfs(grph,st):
    visited = [False]*(v+1)
    visited[0] = True
    queue.append(st)
    while queue:
        x = queue.pop(0)
        visited[x] = True
        for i in adj_list[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                parent_list[i] = x


ans = bfs(adj_list,1)
path = []
count = -1

while need is not None:
    path.append(need)
    need = parent_list[need]
    count+=1

task5_output.write(f"Time: {str(count)}\n")
task5_output.write(f"Shortest Path: ")
for i in range(len(path)-1,-1,-1):
    task5_output.write(str(path[i]) + " ")