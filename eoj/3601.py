#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def main():
    pn, ln = map(int, input().split())
    if ln == 1:
        print(input())
        exit()
    dic = dict()
    endl = set()
    for i in range(pn):
        # one picture
        temp = [input() for j in range(ln)]
        # first line
        dic[temp[0]] = temp
        endl.add(temp[-1])
    head = (set(dic) - endl).pop()
    print(dic[head][0])
    while head in dic:
        temp = dic[head]
        print('\n'.join(temp[1:]))
        head = temp[-1]

main()