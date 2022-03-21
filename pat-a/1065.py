#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    a, b, c = map(int, input().split())
    cmp = 'true' if a + b > c else 'false'
    print(f'Case #{i+1}: {cmp}')