#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
class Num:
    def __init__(self, n):
        self.n = int(n)
        self.f = int(n.replace("-", "")[0])

    def __lt__(self, other):
        if self.f > other.s:
            return True
        elif self.f == other.s:
            return self.n < other.n

def main():
    n = int(input())
    for i in range(n):
        input()
        sl = input().split()
        sl = [Num(k) for k in sl]
        sl.sort()
        print(f"case #{i}:")
        r = [str(k.n) for k in sl]
        print(' '.join(r))

main()