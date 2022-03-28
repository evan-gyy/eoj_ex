#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
morse_code = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G",
"....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N",
"---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T",
"..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
"-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5",
"-....":"6","--...":"7","---..":"8","----.":"9","/////":'.',"///":' '}
for i in range(int(input())):
    print(f'case #{i}:')
    s = input()
    info = ''
    temp = ''
    for j in s:
        if j != '/':
            if set(temp) == {'/'}:
                if temp.count('/') != 1:
                    info += morse_code[temp]
                temp = ''
            temp += j
        else:
            if set(temp) != {'/'}:
                info += morse_code[temp]
                temp = j
            else:
                temp += j
    if temp and temp != '/':
        info += morse_code[temp]
    print(info)