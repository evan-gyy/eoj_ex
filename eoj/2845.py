#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
left, right = input().split('=')
a = ''
def parser(s):
    global a
    temp = ''
    dic = {'num': 0}
    for i in s:
        if not temp:
            temp += i
        elif i in ['+', '-']:
            if 'a' <= temp[-1] <= 'z':
                a = temp[-1]
                x = temp[-1]
                if len(temp) == 1:
                    result = 1
                elif len(temp) == 2 and temp[-2] in ['+', '-']:
                    result = eval(temp[-2] + '1')
                else:
                    result = eval(temp[:-1])
                if x in dic:
                    dic[x] += result
                else:
                    dic[x] = result
            else:
                dic['num'] += eval(temp)
            temp = i
        else:
            temp += i
    if temp:
        if 'a' <= temp[-1] <= 'z':
            a = temp[-1]
            x = temp[-1]
            if len(temp) == 1:
                result = 1
            elif len(temp) == 2 and temp[-2] in ['+', '-']:
                result = eval(temp[-2] + '1')
            else:
                result = eval(temp[:-1])
            if x in dic:
                dic[x] += result
            else:
                dic[x] = result
        else:
            dic['num'] += eval(temp)
    return dic

ld, rd = parser(left), parser(right)
x = 0
num = 0
for k, v in ld.items():
    if k == 'num':
        num -= v
    else:
        x += v
for k, v in rd.items():
    if k == 'num':
        num += v
    else:
        x -= v
print('{}={:.3f}'.format(a, num / x))



