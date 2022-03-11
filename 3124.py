#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: evan-gyy
import re
for i in range(int(input())):
    s = input()
    res = re.sub(',|\.|!|\?', ' ', s).split()
    while ' ' in res:
        res.remove(' ')
    res = list(set(res))
    print('case #{}:'.format(i))
    print(' '.join(sorted(res)))