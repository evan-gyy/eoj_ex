#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n, kk, m = map(int, input().split())
full = list(map(int, input().split()))
dic = {}
for _ in range(m):
    user, prob, score = input().split()
    if user not in dic:
        dic[user] = ['-'] * kk + [0] * 2
    if score != '-1':
        if dic[user][int(prob)-1] != '-':
            score = max(int(score), dic[user][int(prob)-1])
    else:
        score = 0
    dic[user][int(prob)-1] = int(score)
for k, v in dic.items():
    for i in range(int(kk)):
        if v[i] != '-':
            v[-1] += int(v[i])
            if int(v[i]) == full[i]:
                v[-2] += 1
dic = dict(sorted(dic.items(), key=lambda x: (-x[1][-1], -x[1][-2], x[0])))
temp = -1
rank = 1
i = 1
for k, v in dic.items():
    if v[-1] != 0:
        if temp != -1:
            if v[-1] != temp:
                rank = i
        print(rank, k, v[-1], ' '.join([str(j) for j in v[:-2]]))
        temp = v[-1]
        i += 1