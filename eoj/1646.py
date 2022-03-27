#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = input()
    for i in range(int(n)):
        start, end = map(int, input().split())
        step = []
        queue = [[[start], 0]]
        while queue:
            curr = queue.pop(0)
            if curr[0][-1] == end:
                step.append(curr[1])
                print(curr[1])
                break
            for j in range(4):
                s = list(str(curr[0][-1]))
                for k in range(1, 10):
                    if s[j] == str(k):
                        continue
                    s[j] = str(k)
                    ss = int(''.join(s))
                    if ss not in curr[0] and is_prime(ss):
                        steps = curr[1] + 1
                        t = curr[0][:]
                        t.append(ss)
                        queue.append([t, steps])
        if not step:
            print("Impossible")

main()
