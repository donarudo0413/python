# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:12:11 2021

@author: DONARUDO
"""

import csv
with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Score']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Mike', 'Score': 90})
    writer.writerow({'Name': 'Bob', 'Score': 95})
