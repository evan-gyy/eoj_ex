#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
l = input().title().split()
l = sorted(set(l))
for i in l:
    print(f"{i[0]}:{i}")