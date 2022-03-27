#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
def main():
    n = int(input())
    for i in range(n):
        s = input()
        print(f"case #{i}:")
        if s.isdigit():
            if set(list(s)) <= {'0', '1'}:
                print(int(s, 2))
            else:
                print(s)
        else:
            l = len(s)
            if l == 1:
                print(1)
            elif l == 2:
                if s[0] == s[1]:
                    print(3)
                else:
                    print(2)
            else:
                nums = [1, 0]
                for num in range(2, 61):
                    nums.append(num)
                dic = {}
                for j in range(l):
                    if s[j] in dic:
                        continue
                    dic[s[j]] = nums.pop(0)
                r = []
                for ss in s:
                    r.append(dic[ss])
                rs = 0
                ad = len(set(list(s)))
                for k in range(len(r)):
                    t = r[len(r) - k - 1]
                    rs += t * ad ** k
                print(rs)

main()