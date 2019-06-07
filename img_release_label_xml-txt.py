#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:43:35 2019

@author: zhu
"""
import os
import sys
import xml.etree.ElementTree as ET
import glob
import numpy as np

indir='/home/zhu/data/img_release_label/'   #xml目录
outdir='/home/zhu/data/img_release_label_txt/'  #txt目录

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')
    print(annotations)
    
    file_save = 'img_release_label_txt.txt'
    file_txt=os.path.join(outdir,file_save)
    f_w = open(file_txt,'w')
    
    for i, file in enumerate(annotations):
#        print(file)
        

        # actual parsing
        in_file = open(file)
#        print(file)
        tree=ET.parse(in_file)
        root = tree.getroot()

        xn = []
        xx = []
        yn = []
        yx = []

        k = 0
        
        for obj in root.iter('object'):
                current = list()
                
                name = obj.find('name').text
                
                
                
                xmlbox = obj.find('bndbox')
#                xn = xmlbox.find('xmin').text
#                xx = xmlbox.find('xmax').text
#                yn = xmlbox.find('ymin').text
#                yx = xmlbox.find('ymax').text
                
                xn.append(xmlbox.find('xmin').text)
                xx.append(xmlbox.find('xmax').text)
                yn.append(xmlbox.find('ymin').text)
                yx.append(xmlbox.find('ymax').text)
                
              
#                print xn
#                f_w.write(name.encode("utf-8")+' ')
#        f_w.write('img_release/' +file.encode("utf-8") + name.encode("utf-8") + ' ' + xn+' '+yn+' '+xx+' '+yx+' '+'\n')
#        f_w.close()
                
        f_w.write('img_release/' +file.split('.')[0].encode("utf-8") + ' ' + name.encode("utf-8") + ' ')
        for obj in root.iter('object'):
            
            f_w.write(xn[k] + ' ' + yn[k] + ' ' + xx[k] + ' ' + yx[k] + ' ')
            k = k +1
            
        f_w.write('\n')

    f_w.close()



xml_to_txt(indir,outdir)
