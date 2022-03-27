#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
for i in range(int(input())):
    n = int(input())
    m = 5
    count = 0
    while n >= m:
        count += n // m
        m *= 5
    print(count)