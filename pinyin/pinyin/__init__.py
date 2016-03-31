#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import re
# if(re.match(u"[\u4e00-\u9fa5]{2,4}$", '东A'.decode('utf8'))):
#     print '1111'    
# else:
#     print '000'
dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
ran_dic=sorted(dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
for k in range(0,len(ran_dic)):
    print ran_dic[k][0]
    print ran_dic[k][1]