#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
class Num:
    def __init__(self, n):
        self.n = int(n)
        if self.n >= 0:
            self.s = bin(self.n)
        else:
            self.s = bin(2 ** 64 + self.n)
        self.one = self.s.count('1')

    def __lt__(self, other):
        if self.one > other.one:
            return True
        elif self.one == other.one:
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
