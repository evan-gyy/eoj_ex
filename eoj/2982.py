# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
def main():
    n = input()
    for i in range(int(n)):
        sl = input().split()[1:]
        sl = [int(i) for i in sl]
        idx = sl.index(-1)
        res = -1
        if idx >= 3:
            res = sl[idx-1] + sl[idx-2] + sl[idx-3]
        else:
            try:
                if idx == 2:
                    res = sl[idx+1] - sl[idx-1] - sl[idx-2]
                elif idx == 1:
                    res = sl[idx+2] - sl[idx+1] - sl[idx-1]
                elif idx == 0:
                    res = sl[idx+3] - sl[idx+2] - sl[idx+1]
            except:
                pass
        if res != -1:
            sl[idx] = res
            for j in range(len(sl) - 3):
                if sl[j] + sl[j+1] + sl[j+2] != sl[j+3]:
                    res = -1
                    break
        if res < 1:
            res = -1
        print(f"case #{i}:")
        print(res)

main()

