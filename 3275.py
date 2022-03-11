#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import datetime
s = input()
try:
    d = datetime.datetime.strptime(s, '%Y-%m-%d').date()
    delta = (d - datetime.date(d.year, 1, 1)).days + 1
    print(delta)
except:
    print(-1)