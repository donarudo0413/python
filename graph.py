# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:12:02 2021

@author: DONARUDO
"""

import numpy as np
import matplotlib.pyplot as plt

m = 100
kukan = 30
cut = int((kukan-1)/2)
x = np.zeros(m)
for i in range(m):
    x[i] = i*i# 数式 x=i^2
y = np.zeros(m)
z = np.zeros(m)
for i in range(m):
    z[i] = i   
for i in range(m):
    if(i>1):
        if(i<m-2):
            y[i] = (x[i-2]+x[i-1]+x[i]+x[i+1]+x[i+2])/5

#各フォント
plt.title("graph", fontsize = 40)
plt.xlabel("i", fontsize = 40)
plt.ylabel("y", fontsize = 40)
plt.tick_params(axis='x', which='major', labelsize=20)
plt.tick_params(axis='y', which='major', labelsize=20)
plt.xticks(np.arange(0,m+1,10))#x軸のメモりの刻み
plt.yticks(np.arange(0,x[m-1]+1,1000))#y軸のメモリの刻み

#グラフ
plt.plot(x,color='red')# 数式 x=i^2
plt.scatter(z[cut:m-cut-1],y[cut:m-cut-1],color='blue')# 移動平均