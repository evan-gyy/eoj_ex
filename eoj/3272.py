#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def judge(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return True
    else:
        return False
n = int(input())
for i in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    def run(m):
        for j in range(m-2):
            for k in range(j, m-1):
                for x in range(k, m):
                    if judge(l[j], l[k], l[x]):
                        return True
        return False
    if run(m):
        print(f'Case {i + 1}: NO')
    else:
        print(f'Case {i + 1}: YES')
