#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def main():
    n = int(input())
    for i in range(n):
        s = input().split()
        ptr = input()
        print(f'case #{i}:')
        print(s.count(ptr))

main()