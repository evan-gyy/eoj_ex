# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
def main():
    input()
    sl = input().split()
    sl = [int(i) for i in sl]
    count = 0
    length = len(sl)
    left = 0
    right = length - 1
    while left < right:
        if sl[left] == sl[right]:
            left += 1
            right -= 1
        elif sl[left] < sl[right]:
            left += 1
            sl[left] += sl[left - 1]
            count += 1
        else:
            right -= 1
            sl[right] += sl[right + 1]
            count += 1
    print(count)

main()