#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:17:22 2019

@author: zhu
"""


#import skimage.io as io
#from skimage import data_dir
#data_dir = '/home/zhu/data/header'
#str=data_dir + '/*.jpg'
#coll = io.ImageCollection(str)
#print(len(coll))
#io.imshow(coll[205])


from skimage import data_dir,io,transform,color
import numpy as np

data_dir = '/home/zhu/data/header'

def convert_resize(f):
#     rgb=io.imread(f)    #依次读取rgb图片
#     gray=color.rgb2gray(rgb)   #将rgb图片转换成灰度图
     image = io.imread(f)
     dst = transform.resize(image,(12,12))  #将灰度图片大小转换为256*256
     return dst
    
    
str=data_dir+'/*.jpg'
coll = io.ImageCollection(str,load_func=convert_resize)
print(len(coll))
for i in range(len(coll)):
#for i in range(2):
    io.imsave('/home/zhu/data/header_resize/'+np.str(i)+'.jpg',coll[i])  #循环保存图片
