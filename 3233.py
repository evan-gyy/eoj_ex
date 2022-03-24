#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
while True:
    try:
        n = int(input())
        k = 0
        m = 5
        while m <= n:
            k += n // m
            m *= 5
        print(k)
    except:
        break