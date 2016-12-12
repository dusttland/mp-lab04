# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:20:06 2016

@author: mihkel
"""

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv'))
header = next(csv_file_object)

data = []
for row in csv_file_object:
    data.append(row)
    
data = np.array(data)

print(data)
