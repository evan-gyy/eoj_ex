#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
while True:
    try:
        s = input()
        level = len(s)
        wave = [[] for _ in range(len(s) * 2 + 1)]
        temp = 0
        for i in range(len(s)):
            if i != 0:
                if ord(s[i]) > ord(temp):
                    level += 1
                if ord(s[i]) < ord(temp):
                    level -= 1
                while len(wave[level]) < i:
                    wave[level].append(' ')
            temp = s[i]
            wave[level].append(temp)
        for i in range(len(wave)-1, -1, -1):
            if len(wave[i]) > 0:
                print(''.join(wave[i]))
    except :
        break