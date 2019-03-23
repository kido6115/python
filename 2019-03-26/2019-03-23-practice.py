import sys
sys.path
sys.path.append(r'C:\Users\user\Desktop\sungyeh\python\2019-03-26')

from myFunction import bmi

import random

choiced=[1,21,45]

needLength=6-len(choiced)

pool=[i for i in range(1,50)]
for i in choiced:
    pool.remove(i)
auto=random.sample(pool,needLength)
final=auto+choiced
