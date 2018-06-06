#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:03:46 2018

@author: raja
"""


def find_feature(box):
        box=np.floor(box)
        box_list=box.ravel()
        hist,bins = np.histogram(box_list.ravel(),360,[0,360])
        
        b_bins=np.zeros(360)
        b_hist=np.zeros(360)
        for i in range(0,360):
            count=0
            for j in range(0,np.size(box_list)):
                if i==box_list[j]:
                    count=count+1
            b_bins[i]=i
            b_hist[i]=count
        
        N_pix= np.size(box)
        N_g= b_hist
        P_g= N_g/N_pix
        g_g= b_bins
       
        his_mean=np.sum(g_g * P_g)+1
        his_SD = np.sqrt((np.sum(np.square(g_g-his_mean)*P_g)))
        his_skew = ((np.sum(((g_g-his_mean)**3)*P_g)))/(his_SD**3)
        his_energy = np.sum(P_g**2)
        his_entropy = -np.sum(P_g*np.log2(P_g+1))
        
        return his_mean, his_SD, his_skew, his_energy, his_entropy
    
