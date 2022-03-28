#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for j in range(n):
        matrix.append([int(x) for x in input().split()])
    first = 0
    second = 0
    size = 0
    def dfs(x, y):
        global size
        matrix[x][y] = -1
        for nx, ny in [(x + 1, y), (x, y + 1),
                       (x - 1, y), (x, y - 1)]:
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    size += 1
                    dfs(nx, ny)
    for j in range(n):
        for k in range(m):
            if matrix[j][k] == 1:
                size = 1
                dfs(j, k)
                if size > first:
                    second = first
                    first = size
                elif first > size > second:
                    second = size
    print(f'case #{i}:')
    print(second)
