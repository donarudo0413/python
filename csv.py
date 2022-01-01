import csv
import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(10)
y = np.zeros(10)
c = 0
with open('data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    next(csv_reader)#ヘッダーを消す
    for row in csv_reader:
        x[c] = row[0]
        y[c] = row[1]
        c += 1
print('x=',x)
print('---')
print('y=',y)
plt.plot(x,y)