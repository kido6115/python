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
Li.append('tist')
Li[5]='test'
Li.append(L1)
Li.extend(L1)
Li.remove('test')
del Li[0:2]

Lab=['a','B','d','d','e','f']

Lab[1]=Lab[1].lower()
Lab[2]='c'
Lab.append('g')
[x for x in Lab]
# copyLab=Lab
copyLab=Lab.copy()
Lab.append('s')
copyLab is Lab

Ln.append('end')
Ln.pop()
Ln.insert(0,'start')
Ln.pop(0)

Ts=(1,2,3,4,5,6,7)
T=('a',) #一元素tuple

s1=set() #empty set
s2={} #empty dict

json={
    'id':11,
    'name':'sungyeh',
    'age':15
}
json2={
    'email':'test@mail.com.tw'
}
json.update(json2)

## Test zip()
m=('a','b','c')
x=(1,2,3,4,5)
y=(5,10,15,20,25)
z=(2,4,6,8,10)
list(zip(m,x,y,z)) #: ?

gp=(x,y,z)
gp_match=list(zip(m,gp)) # basic data structure for a dataframe

# 009-4 字典的應用
## define 4 variables
var=('name','gender','english','math')

## 7 observations for each variable
gender=('M','M','M','M','F','M','F')
math=(35,77,69,81,55,47,83)
english=(68,81,60,92,72,33,65)
name=('Georgie','Derek','Dan','Sting','Jade','Anthony','Beth')

## put the content together
table=(name,gender,english,math)

## create dict by zip() function
list(zip(var,table))
record=dict(zip(var,table))

import pandas as pd
record_df=pd.DataFrame(record) #: create a dataframe
# r:handle windows path back-slash
record_df.to_csv(r"C:\Users\user\Desktop\pythontest.csv",index=False)
record_df = pd.read_csv(r"C:\Users\user\Desktop\pythontest.csv")
test=pd.read_csv("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv")


x=int(input('input score:'))

if x>100:
    print('還想騙阿')
elif x==100:
     print('好棒棒')
elif x>=90:
     print('人才!')
elif x>=80:
     print('嘉勉')
elif x>=70:
     print('po ton')
else:
    print('請大俠重新來過')

for i in {1,2,3,4,5}:
    print(i)    
    
for i in range(2,8,2):
    print(i)  

returnList=[c*5 for c in range(5)]
newList=[]
for i in range(5):
    newList.append(i*5)

for i in range(1,10):
    for j in range(1,10):
        if j==4:
            break
        print(f'{i} * {j} = {i*j:2d}')

a=13580
b=0.8739
print(f'a={a:,}\nb={b:.1%}\na x b={a*b:,.2f}')

subI=0
while subI<9:
    subJ=0
    while subJ<9:
        if subJ==4:
            break
        print(f'{subI+1} * {subJ+1} = {(subI+1)*(subJ+1):2d}')
        subJ+=1
    subI+=1

def method(x,y):
    x=x**2
    y+=2
    return (x,y)
method(2,4)