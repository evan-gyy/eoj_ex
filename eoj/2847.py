#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import math
n = int(input())
r = math.factorial(n) / (24 * math.factorial(n - 4))
print(int(r))