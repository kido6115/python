# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:45:17 2018

@author: Bing-tsu Chang
"""

# 000 Python 起手式
#-------------------------------------------------------
## 檢查一下 Python 版本先
import sys # 匯入 Python 內建模組 sys
sys.version

## 我的第一行程式
print('My first Python code')
print('I come,','I see,','I conquer!')


# 001 變數
#-------------------------------------------------------

a=3
b=5
b=b+8

print(a,b) # '=' 是指派一個 '值' 給一個變數的意思
c='My first line of Phthon code'
print(c) # 變數也可以是 '字串'

## 變數名稱可以是字母 (大、小寫敏感)、數字或符號，但起始字元必需是英文字母

## 檢查不能使用的保留字
import keyword # 匯入 Python 內建模組 keyword
keyword.kwlist

# 002 數字計算 加減乘除
#-------------------------------------------------------

x1=b-a
x2=b*a
x3=b/a
print('x3=',x3)
print('取整數：',int(x3))
print(round(x3))
print(round(x3,3)) # round                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

## 次方

b**2
b**3

## 開根號
b**0.5
8**(1/3)

## 其它運算
print(a,b)

b%a # 餘數, mold (模)
b//a # 整數商

print(-8//3,-8%3) # 這要如何解釋? "向下整除"

## 
a+=1 #a=a+1
a-=1 #a=a-b

## 二進制異位
a^b
bin(a)
bin(b)

## int() 與 round()
x3=33/a
print(x3)
print(int(x3))
print(round(x3)) #? 四捨五入? try round(2.5)，and round(3.5)

## 列印換行控制
print(a)
print(b)
print(a,b,c)

print(a,end='') # 列尾 end='':移除跳行指令
print(b,end=',')
print(a)

print(a,b,'\n',c) # '\n':強迫換行

## 邏輯運算 ==、!=、>、<、>=、<=
a%2==1
b%2==1

# 003 變數型態
#-------------------------------------------------------
a=8 #: int
b=3.8 #: float
c,d='abc','True' #: str
t,f=True,False #: boolean
print(a,b,c,d,t,f)
type(d)
type(t)

# 003-1 字串運算
#-------------------------------------------------------
s1=c+d
s2=s1*5
print('s1=',s1)
print('s2=',s2)

s1.upper()
s1.lower()
s1.capitalize()

# 003-2 布林運算
#-------------------------------------------------------
print(t,f)
b1=not t
b2=t and f
b3=t or f
print (b1,b2,b3)

## 布林運算順序
not f or t and f # 如果依先後順序計算，應該是以下結果：
((not f) or t) and f # 實際運算順序 not > and > all

## 布林值乘法
t*3
t/3 # True has a value of 1

# 004 Python 內建容器　built-in Containers
#-------------------------------------------------------
## 字串 str''
## 列表/串列 list[] # 主要處理數據的工作區
## 數組　tuple()
## 集合　set{value}
## 字典　dict{'key':value} # 建置數據結構的工作區

# 004-1 有序與索引:以 str 字串為例
#-------------------------------------------------------
s1='abcdefgh'
s1[3]

'''
s1[index]
index：start form 0
str,list,tuple 均為有序數列, 適用索引 [index]
set,dict 為無序數列, 不適用索引
'''
## 多列註解: 前後以三重引號包夾

## 反向 index:
print(s1[-1],s1[-2])

# 005 list 列表 [] 基本運算與索引
#-------------------------------------------------------
Ls=['apple','orange','banana','pear','banana']
Ln=[1,2,2,3,4,5,5,'6','7','7',8,9]
Lb=[True,False]

## 以加號合併: 
Lc=Ls+Ln+Lb

## 以列表合併:
Ld=[Ls,Ln,Lb]

## 列表乘以整數:
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

Li[2::3] # [開頭(預設0):結尾(預設-1):間隔(預設1)] 語法
Li[6:3:-1]


# 006 list 編輯功能
#-------------------------------------------------------

# 006-1 index 查詢 value 的索引位置
Ls.index('banana') 
Ln.index(5,2,6)# (value,start,end)
## list.command 是 Python 執行內建 method 的基本語法

#-------------------------------------------------------

# 006-2 count 計算 value 的出現次數
## list.count(value)

#-------------------------------------------------------

# 006-3 取得 list 的長度
## 好像很容易，來猜猜看?

#-------------------------------------------------------

# 006-4 basic list editing
## mutability：list is a mutable object
## 列尾增添：list.append(new value)
## 列中插入：list,insert(index, value)
## 直接修改：list[index]='new value'

#-------------------------------------------------------

# 006-5 extend
#: extend 與 append　有何不同? 
#: append 將容器視為 _______ 添加於列尾
#: extend 將容器 ________ 添加於列尾

#-------------------------------------------------------

## example
L=['abcdefadfg']
L=list('abcdefadfg') # 兩者有何差別 ?

L.index('d')
L.index('d',4)
L.count('d')
L.append('h')
L.insert(3,'x')
L.extend('i') # same as append?
L.append('mno')
L.extend('pqr')
len(L)
p=[['a','b'],['c','d']]
L.append(p)
L.extend(p)

#-------------------------------------------------------

## Practise
## Lab 是一個應該包含 a~g 連續小寫英文字母的串列，但因為輸入錯誤，結果如下： 

Lab=['a','B','d','d','e','f']

#:請使用以上的 list 編輯指令，將 Lab 清理為 ['a','b','c','d','e','f','g']
Lab[1]='b'
Lab.insert(2,'c')
del Lab[3]
Lab.append('g')
print (Lab)

#-------------------------------------------------------

# 006-6 自串列中移除元素
## list.remove(value)
print(L)
L.remove('a')

## del list[index]
del L[3]
del L[2:4]


#-------------------------------------------------------

# 006-7 清空與移除clear() 移除與清空
## list.clear()
print(L)
L.clear()
## del list
del L

#-------------------------------------------------------

# 006-8 兩種複製 shallow and deep 
## shallow copy 副本與原始物件不連動
## deep copy 副本與原始物件連動

## b=a.copy() shallow copy
a=[1,2,3]
b=a.copy()
print(a,b)
a is b # check

a.append(4)
print(a,b)

b.append(5)
print(a,b)

## b=a deep copy
a=[1,2,3]
b=a
print(a,b)
a is b # check

a.append(4)
print(a,b)

b.append(5)
print(a,b)

#-------------------------------------------------------

# 006-9 pop() 自列尾（或指定索引）移除並回傳
print(Ln)
a=Ln.pop()
a=Ln.pop(0)
## 這裡因為是函數 pop()的表述，依據其定義，索引不用再加方括號 []

#-------------------------------------------------------

# 006-10 建立空串列備用
## 別小看這一招，是很多程序的基礎，很常用，很好用！
Le=[]
Le.append(1)

#-------------------------------------------------------


# 007 堆疊 stack 與佇列 Queue
#-------------------------------------------------------

## 堆疊 後進先出
## 佇列 先進先出
print(Ls)
import collections
Lq=collections.deque(Ls)
## deque' stands for 'double-ended queue'
Lq.append('pineapple') # 添加元素在列尾
Lq.popleft() # 自列頭取出最先添加的元素
## Queue型態的數列，兩端都可以添加或取出元素
## 以上功能是希望能彈性的從列頭或列尾添加、回傳並移除元素
## 但其實有更簡單的方法，所以掠過

## list.append()、list.pop() 預設僅從列尾添加、回傳並移除元素
# 要如何從列頭添加、回傳並移除元素 ?
print(Ln)

Ln.append('x') # 自列尾添加元素
Ln.pop() # 自列尾回傳並移除

## 如果要從列頭添加或移除，可以怎麼辦 ?

Ln.insert(0,'a') # 自列頭添加
Ln.pop(0) # 自列頭回傳並移除

print(Ln)
('a','b','c',1,2,3,True,False)

# 008 tuple 數組 ()
#-------------------------------------------------------

# 008-1 tuple 特性
## 不能增, 減, 或執行任何內容編輯
## 元素為有序排列
## 由於不能編輯內容, 所以通常用在計算完以後的儲存容器, 可以避免錯誤
## 在大量迭代 iteration 時, 較 list 省系統資源

#-------------------------------------------------------

# 008-2 建立 tuple
Ts=('apple','orange','banana','pear','banana')
Tn=(1,2,3,4,5,5,6,7,8,9)
Tb=(True,False)
Tc=(Ls,Tn,True,3,'e')
Td=1,2,3
type(Td)

#-------------------------------------------------------

# 008-3 tuple, list, 以及後面要說的 set, 都是指令, 可改變數列的形式
Tuple_s=tuple(Ls) 
List_s=list(Ts)
set_s=set(Ts) #: 元素少了一筆 ?

#-------------------------------------------------------

# 008-4 檢驗元素是否包含在數列中
print(Tuple_s)
print(List_s)
'orange'in Tuple_s
'orange' in List_s
## 可否檢驗到第二層 ? 
Ld=[Ls,Ln,Lb]
True in Ld
[True, False] in Ld

#-------------------------------------------------------

# 008-5 單一元素 tuple 與字串
Tsingle=('abc') # it's a string
Tsingle=('abc',) # it's a tuple
## 可以 type() 檢驗

#-------------------------------------------------------

# 009 set 集合 與字典 dict {}
#-------------------------------------------------------

# 009-1 集合
## 集合中的元素無序，且不可重複

S1=set() #: 創建空集合
S2={}
type(S1)
type(S2)

S1.add(1)
L5=[2,3,4,5,6,6,7,8,9,9]
S1.update(L5)

## unique elements only
S1.add(['a','b','c']) #? unhashable ?
S1.add(('a','b','c'))

## try slicing by index
S5[3] #: TypeError，set 無序

#-------------------------------------------------------

# 009-2 集合的邏輯運算
S1={1,2,3,4,5,6,}
S2={4,5,6,7,8,9,}

Su=S1|S2 #union
Si=S1&S2 #intersection
Sd12=S1-S2 #difference
Sd21=S2-S1 #difference
Sun=S1^S2 #unique elements

#-------------------------------------------------------

# 009-3 創建字典

D={} # 創建空字典

'''
字典結構
dict={'key 1':value 1,
      'key 2':value 2,
                .....,
      'key n':value n}
'''

## 3 Ways to add content into a Dict 
S3={
    'obvs':('a','b','c','d','e','f'),
    'x1':(1,2,3,4,5,6)
    }

S3.update({'x2':(10,20,30,40,50,60)})

S3['x3']=(True,False,False,True,True,True)

## index with 'Key'
S3['x3']

#-------------------------------------------------------

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

## python dict 和 json 結構相同
## 但 json 僅為一字串，而 dict 是含功能結構的數據組

#------------------------------------------------------- 

## Test zip()

m=('a','b','c')
x=(1,2,3,4,5)
y=(5,10,15,20,25)
z=(2,4,6,8,10)
list(zip(m,x,y,z)) #: ?

gp=(x,y,z)
gp_match=list(zip(m,gp)) # basic data structure for a dataframe

#-------------------------------------------------------

# 009-5 introduction of DataFrame and Pandas
import pandas as pd
record_df=pd.DataFrame(record) #: create a dataframe

## adjust columns

record_df=record_df[['name','gender','english','math']]

#-------------------------------------------------------

# 009-6 數據匯出 / 入

## send csv file out
record_df.to_csv(r"C:\Users\user\Desktop\Ben\pythontest.csv",index=False)
## try to remove the index

## read csv file in 
record_df = pd.read_csv(r"C:\Users\user\Desktop\Ben\pythontest.csv")
type(record_df)

#-------------------------------------------------------

# 010 控制結構
#-------------------------------------------------------

# 010-1 邏輯判斷運算元
## a=b 將 b 的值指派給 a
## a==b 判斷 a、b 是否相等
## 還有其他的判斷運算元，請參考 講義 P 22

#-------------------------------------------------------

# 010-2 if 判斷

x=int(input('請輸入成績:'))

if x>100:
    print('Wrong entry,Try again!')
elif x==100:
    print('Perfect!')
elif x>=80:
    print('good!')
elif x>= 60:
    print('Average!')
else:
    print('You need to stydy harder!')

## 請默寫一次，根據以上語法，自設一個判斷的題目，寫一個 if 判斷

#-------------------------------------------------------
    
# 010-3 for 迴圈
for i in [1,2,3]:
    print('Route:',i) # 在後面加上 end='', 看看有什麼不同
    print(' Value:',i*2)
    
## for in in (範圍)，(範圍) 可以是序列元素、可迭代數列、range()

a=[1,2,True]
for i in a:
    print('Route:',i)
    print('Value:',i*2)
## list 可以，tupple 或 set 可以當(範圍)嗎?
## 數字可以，文字可以嗎?
## 布林值可以嗎?
## 布林值拿去運算，會怎樣?
    
## 範圍如果用 range() 
## rantg(n) 表示從 0 到 n-1，共 n 項
## range()還有哪些可能?
## 自訂起、止? 調整間隔? 倒數?

for i in range(5):
    print(i)

#-------------------------------------------------------  
    
# 010-4 列表推導式 list comprehension

lc=[i for i in range(10)] #: basic
print(lc)

lca=[a*j for a in ('x','y','z') for j in range(1,4)] #: multiple loop
print(lca)

lcb=[[a*j for a in ('x','y','z')] for j in range(1,4)] #: multiple layer
print(lcb)

## 練習-請用列表推導式,寫一個包含九九乘法表所有結果的陣列

#-------------------------------------------------------

# 010-5 while 迴圈
#-------------------------------------------------------

x=1 # 迴圈外，需設定起始值

while x<=10: # 起始值符合,條件判斷為 True，否則不會執行
    print('Route:',x)
    x=x+1 # 迴圈內一定要有脫離的機制，否則會無限循環
    # 縮排表示執行區塊
    # 多重迴圈即以縮排來表示迴圈層

print('---------------------') # 縮排結束，表示已離開迴圈
print('Out of loop:',x)

#-------------------------------------------------------

# 010-6 字串格式 f-string

a=13580
b=0.8739
print(f'a={a:,}\nb={b:.1%}\na x b={a*b:,.2f}')

## 練習-請用 while 迴圈寫一個九九乘法表，並用 f-string 顯示結果

i=2
while i<=9:
    j=1
    while j<=9:
        print(i*j)
        j=j+1
    i=i+1
    
#-------------------------------------------------------

# 010-7 強迫跳過 continue 與強迫脫離 break
## 分別以 for 及 while 迴圈，試寫乘數 (j) 逢 4 中止
## 分別以 for 及 while 迴圈，試寫乘數逢 4 跳過
## 以 f-string 修飾印出結果
## while 迴圈乘數逢 4 跳過    

for i in range(2,10):
    for j in range (1,10):
        if j==4:
            break # try another command:continue
        print(f'{i} X {j} = {i*j}')



i=2
while i<=9:
    j=1
    while j<=9:
        if j==4:
            break # try continue ???
            #print('------ skip ',j)
            #j=j+1 # must have
            #continue
        print(f'{i}x{j}={i*j:2d}')
        j=j+1
    i=i+1    
    
#-------------------------------------------------------
# 綜合練習 1:計算兩數的最大公約數 
#-------------------------------------------------------

# 013 函數基本形式與語法
#-------------------------------------------------------
## 沒有參數，執行指定動作，沒有傳回值
def f0():
    print ('沒有參數，執行指定動作，沒有傳回值')
f0()

## 沒有參數，執行指定動作，有傳回值
def f1():
    print('沒有參數，執行指定動作，有傳回值')
    return(3.1416)
f1()  

## 傳遞參數

a,b=20,30 # 全局變數

def f2(x,y):
    print ('有參數，無預設值，執行指定動作，有傳回值')
    a=x+2
    b=y*2
    return(a,b) # 局部變數

f2(3,5)
res_l=f2(3,5)
v1,v2=f2(3,5)  

print(a,b)

## 傳遞參數，參數有預設值，執行指定動作，有傳回值
def f3(x,y,z=12):
    print ('傳遞參數，參數有預設值，執行指定動作，有傳回值')
    a=(x+y)/z
    return(a,z)
f3(2,4)
f3(3,5,2)

fn=f3
fv=f3(3,5,2)

## 這樣會有問題

def f4(x,b=2,y,c=3):
    print ('傳遞參數，預設值參數位置穿插，執行指定動作，有傳回值')
    x=x*b
    y=y+c
    return(x,y)

## 傳遞參數，預設值參數置後依序排列，執行指定動作，有傳回值

def f4(x,y,b=2,c=3):
    print ('傳遞參數，預設值參數置後依序排列，執行指定動作，有傳回值')
    x=x*b
    y=y+c
    return(x,y,b,c)
f4(5,10)
f4(5,10,4)
f4(5,10,4,8)

## 參數順序可以自訂
def printme(name,age=35 ):
   print (name,age)
   
printme(age=50,name='John') #: 參數順序可以自訂

## 不確定數量的參數 *args and **kwargs
def f5(*args,**kwargs):
    return args,kwargs

m,n=f5(3,5,6,a=3,b=7)

m[1]
n['a']

#-------------------------------------------------------
# 綜合練習 2 BMI Calculator
#-------------------------------------------------------

## 建立自己的公用模組

import sys
sys.path
sys.path.append(r'C:\Users\user\Desktop\Ben\PythonR2')

#-------------------------------------------------------

# 013-1 遞迴函數與運算效能管理

## fibonacci numbers
## 費波納契數列 (黃金分割數列) 每數為前兩數加總之數列

## 以遞迴函數定義 fib()
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        

## 執行 fib()
for i in range (10):
    print(f'{fib(i)},',end='')

## 當專案規模擴大時，Performance 可能會成為問題

## 計算運算時間
## 加上執行計時器

import time
tStart = time.time() # 計時開始
 
print(fib(10)) # 以 fib() 函數執行任務

tEnd = time.time() # 計時結束

print (f'Time consumed:{tEnd-tStart:.10f} sec.') # 計算耗時

## 用另一種方式計算費波納契函數
## 定義 fib2() 函數，放棄遞迴結構

def fib2(n):
    fib_to=[0,1]
    if n==0:
        return fib_to[0]
    elif n==1:
        return fib_to[1]
    else:
        for i in range(2,n+1):
            fib_to.append(fib_to[i-1]+fib_to[i-2])
        return fib_to[-1]


#加上執行計時器
tStart = time.time() # 計時開始
 
print(f'{fib2(100):,}') # 以 fib2()函數執行任務

tEnd = time.time() # 計時結束

print (f'Time consumed:{tEnd-tStart:.10f} sec.') # 計算耗時

#-------------------------------------------------------
# -End- of Basic Syntax
# Python 3
#-------------------------------------------------------
  
# 綜合練習 1
## 計算兩數的最大公約數

n1=int(input('請輸入第一個數字：'))
n2=int(input('請輸入第二個數字：'))

if n1 < n2:
    n1,n2 = n2,n1

while n2!=0:
    r=n1%n2
    n1,n2=n2,r

print(n1)

#-------------------------------------------------------  
# 綜合練習 2
## BMI Calculator

def bmi(h,w):
    x=w/(h/100)**2
    return x

## 可否將輸出，弄得更人性化一點？

#-------------------------------------------------------  

# 綜合練習 3
## 樂透號碼產生器

## Part II 自選號確定下，產生剩餘號碼

import random # python 內建模組

self_s=[13,17,22] # for test

sl=6-len(self_s) # 系統選號數目

pool=[i for i in range(1,50)] # 1-49 pool
for i in self_s:
    pool.remove(i)

## 將自選號移除後，以隨機選號選出剩餘號碼

auto_s=random.sample(pool,sl)

final=self_s+auto_s # 合併自選號與系統選號
final.sort() # 排序後印出
print(final)

## Part I 自選號的輸入及防錯流程

self_s=[]
for i in range(1,7):
    try:
        while True:
            x = int(input(f'請輸入第 {i} 組號碼(直接 Enter 即結束輸入):'))
            if x > 49:
                print('數字不能大於49')
            elif x in self_s:
                print(f'重複輸入{x}')
            else:
                break
        self_s.append(x)
    except ValueError:
        break
print(self_s)

## 試建立一個函數，呼叫時可傳入不定數量的自選號，並放入自訂模組
from myfunc import *
lotto(3,5)

#-------------------------------------------------------

# 014 基本繪圖　matplotlib 套件
import matplotlib.pyplot as plt
plt.scatter(record_df['math'],record_df['english'])
plt.xlabel('math')
plt.ylabel('english')

plt.boxplot([record_df['math'],record_df['english']],
            labels=['math','english'])

# End of Basic Python Syntax Practise------------------------------