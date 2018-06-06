import cv2 as cv2
import numpy as np
from skimage import io,color
from skimage import data
from matplotlib import pyplot as plt
from skimage.measure import regionprops
from skimage import measure
from skimage import filters
import scipy


t= io.imread('plate2.jpg')
#t= io.imread('yellowboard.jpg')
#t= io.imread('test2.jpg')

r=t[:,:,0]
g=t[:,:,1]
b=t[:,:,2]
 
pic=np.copy(b)
val = filters.threshold_otsu(pic)
ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY)
io.imshow(th1)

plt.figure()
plt.hist(th1.ravel(),256,[0,256]); plt.show()

b_ones= np.count_nonzero(th1!=0)
b_zeros= np.count_nonzero(th1==0)

if b_ones < b_zeros:
    print('YELLOW YELLOW YELLOW Background')
else:
    print('WHITE WHITE WHITE Background')