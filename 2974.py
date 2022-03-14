#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
n = int(input())
stopwords = ['the', 'a', 'an', 'of', 'for', 'and']
for i in range(n):
    s = input().lower().split()
    count = 0
    for j in s:
        if j not in stopwords:
            count += 1
    print(f"case #{i}:")
    print(count)
