#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def main():
    res = [1, 2]
    a, b = 1, 2
    for i in range(99998):
        t = a + b
        res.append(hash(t))
        a, b = b, t
    while True:
        try:
            n = int(input())
            print(res.index(hash(n)) + 1)
        except:
            break


main()