#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:43:35 2019

@author: zhu
"""
import numpy as np
#import cv2

with open('label.txt', 'w') as f:
    for i in range(5397):
        f.write('header_resize/' + np.str(i) + '1' + ' ' + '1' + ' ' + '1' + ' ' + '10' + ' ' + '10\n')
    f.close()