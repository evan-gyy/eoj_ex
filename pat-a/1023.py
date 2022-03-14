#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
s = input()
ss = str(int(s) * 2)
if len(set(s)) == len(set(ss)):
    print('Yes')
else:
    print('No')
print(ss)