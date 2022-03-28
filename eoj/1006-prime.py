#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
try:
    is_prime = [1] * 1000000
    prime = {0:0, 1:0}
    count = 0
    for i in range(2, 1000000):
        if is_prime[i]:
            count += 1
            for j in range(i*i, 1000000, i):
                is_prime[j] = 0
        prime[i] = count

    while True:
        n, m = [int(i) for i in input().split()]
        print(prime[m] - prime[n-1])

except:
    pass