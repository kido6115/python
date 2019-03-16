# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:06:11 2019

@author: user
"""

import sys # 匯入 Python 內建模組 sys
import keyword
t,f=True,False

sys.version
print('Hello World!')

a=3
x=a+3
print('x=',x)
#保留字
#print(keyword.kwlist)
round(3.5)
c='foo'
print(a,x,c)
print(a,end='@')
print(x,end='@')
print(c)
d=.14
str='BaR'
str.capitalize()
# 負索引
str[-1]
Ls=['apple','orange','banana','pear','banana']
Ln=[1,2,2,3,4,5,5,'6','7','7',8,9]
Lb=[True,False]
Lc=Ls+Ln+Lb
Ld=[Ls,Ln,Lb]
Lb*3

## list 索引 (index) 應用
L1=list('abcd')
L2=list('xyz')
print(L1,L2)
Li=[L1,1,2,3,4,5,L2]
print(Li)

Li[0] # start from 0
Li[1:3] # first index included, last index excluded
Li[0][2] # 雙重索引
Li[:2] # 從頭開始
Li[2:] # 至結尾
Li[-1] #反向索引
Li[:3] # 前三項
Li[-3:] # 後三項
Li[2:6:2] # 第三個為間隔
Li[6:3:-1]

Ls.index('banana') 
Ln.index(5,2,6)# (value,start,end)
Ls.count('banana')
