# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
def main():
    n = input()
    for i in range(int(n)):
        sl = input().split()
        def cal():
            next = sl.pop(0)
            if next in ['+', '-', '*', '/']:
                return str(eval(cal() + next + cal()))
            return next
        print('case #{}:'.format(i))
        print('%.6f' % float(cal()))

main()
