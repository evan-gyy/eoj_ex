#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
n = input()
res = []
sum = 0
for i in n:
    sum += int(i)
for i in str(sum):
    res.append(nums[int(i)])
print(' '.join(res))