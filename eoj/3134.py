#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    print(f'case #{i}:')
    order = [1, 3, 5, 4, 2]
    s = list(input())
    new = [s[order[j] - 1] for j in range(5)]
    num = int(''.join(new))
    print(str(num**5)[-5:])