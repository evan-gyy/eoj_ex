#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
count = 0
for i in range(1, int(input()) + 1):
    count += str(i).count('1')
print(count)