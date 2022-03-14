#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
group = []
def sort(ls, loc):
    ls.sort(key=lambda x: x[0])
    ls.sort(key=lambda x: x[1], reverse=True)
    for j in range(len(ls)):
        if j == 0:
            ls[j][loc] = 1
        else:
            if ls[j][1] == ls[j - 1][1]:
                ls[j][loc] = ls[j - 1][loc]
            else:
                ls[j][loc] = j + 1
for i in range(int(input())):
    g = []
    for j in range(int(input())):
        id, score = map(int, input().split())
        g.append([id, score, 0, i+1, 0])
    sort(g, 4)
    group.append(g)
total = sum([len(i) for i in group])
tl = []
for i in group:
    for j in i:
        tl.append(j)
sort(tl, 2)
print(total)
for i in tl:
    print(i[0], i[2], i[3], i[4])
