# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
class Solution:
    def __init__(self):
        self.count = 0
        self.res = 0

    def reverse(self, n):
        n = str(n)
        res = ''
        for i in range(len(n)):
            res += n[len(n) - i - 1]
        return int(res)

    def judge(self, n):
        if n == self.reverse(n):
            self.res = n
            return 0
        self.count += 1
        return self.judge(n + self.reverse(n))

    def main(self):
        n = int(input())
        self.judge(n)
        print(self.count, self.res)

sol = Solution()
sol.main()