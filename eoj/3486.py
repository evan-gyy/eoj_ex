# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
def main():
    s = input()
    if len(set(list(s))) == 1:
        if s[0] == '0':
            print(s[0])
        else:
            print(s)
        return 0
    ms = max(s)
    all = []

    count = 0
    for i in list(s):
        if i == ms:
            all.append(count)
        count += 1

    value = ms
    start = all[0]
    end = all[0]

    for idx in all:
        flag = 0
        res = s[idx]
        for i in range(idx + 1, len(s)):
            curr = s[idx: i+1]
            if curr > value:
                flag = 1
                value = curr
                end = i
        if flag:
            start = idx

    res = s[start: end + 1]
    while True:
        if res[-1] == '0' and len(res) > 1:
            res = res[:-1]
        else:
            break

    print(res)

main()