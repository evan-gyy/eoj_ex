#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
l = []
for i in range(int(input())):
    l.append(int(input()))
l.sort()
for i in range(int(input())):
    print(l[int(input())-1])