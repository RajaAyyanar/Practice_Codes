#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:10:52 2018

@author: raja
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:47:25 2018

@author: raja
"""


from skimage import io 
from skimage import color
from matplotlib import pyplot as plt
import numpy as np

from scipy import ndimage


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
    



#FEATURES OF TARGETTTTTT
def find_full_feature(raja1):
        #raja1= io.imread('/home/raja/Mod 7/test pics/potter.jpg')
        #raja1=color.rgb2gray(raja1)*255
        pic=np.copy(raja1)
        
        pic=pic.astype(float)
        
        mask1=np.array([[1,0,-1]])
        mask2=np.array([[1],[0],[-1]])
        
        mask1=mask1.astype(float)
        mask2=mask2.astype(float)
        
        c1=ndimage.convolve(pic,mask1)
        c2=ndimage.convolve(pic,mask2)
        
        #io.imshow(c1)
        #io.imshow(c2)
        I1=c1.astype(float)
        I2=c2.astype(float)
        
        G=np.sqrt(np.square(I1)+np.square(I2))
        
        #acc= I2/(I1+0.0000000001)
        #theta= np.arctan(acc)
        theta= np.arctan2(I2,I1)
        mod_G=G.astype(np.uint16)
        
        theta_deg= np.rad2deg(theta)
        r,c = np.shape(theta_deg)
        
        
        for i in range(0,r):
            for j in range(0,c):
                if theta_deg[i,j]<0:
                    theta_deg[i,j]=theta_deg[i,j]+360
        
        
        pic=np.copy(theta_deg)
        result_pic=np.zeros(np.shape(theta_deg))
        features_full=np.zeros((np.int(np.floor(r*c/6)),6))
        k1=8;k2=8;k=0
        test_feature=np.zeros((1,5))
        for i in range(0,r,8):
            for j in range(0,c,8):
                pic2= pic[i:i+k1,j:j+k2]
                features_full[k,0:5]=find_feature(pic2)
                #test_feature[0,0:5]=find_feature(pic2)
                #result_pic[i:i+k1,j:j+k2]=svm1.predict(test_feature)
                features_full[k,5]=0
                k=k+1
                
        #mean_feature= np.mean(features_full,axis=0)
        return features_full
        




tar= io.imread('/home/raja/Mod 7/test pics/face_255.png')
tar=color.rgb2gray(tar)*255
target_feature_X= find_feature(tar)

full_pic=io.imread('/home/raja/Mod 7/test pics/full_255.png')
full_pic=color.rgb2gray(full_pic)*255
r1,c1 =np.shape(full_pic)

features_full=[]
kk1,kk2 = np.shape(tar)
#kk1=8;kk2=8;
kk=0
test_feature=np.zeros((1,5))
min_dis=10000
check=0
for i in range(0,r1-kk1,8):
    for j in range(0,c1-kk2,8):
        fpic2= full_pic[i:i+kk1,j:j+kk2]
        fft=[find_mean_feature(fpic2)]
        features_full.append(fft)
            
        check=check+1
        print(check,' out of ',(r1-kk1)*(c1-kk2)/64)
        fft2=np.array([fft])
        #result_pic[i:i+k1,j:j+k2]=svm1.predict(test_feature)
        
        dist = np.linalg.norm(fft2-np.array([target_feature_mean]))
        if dist <= min_dis:
            min_dis=dist
            found_pic=fpic2
            
        








