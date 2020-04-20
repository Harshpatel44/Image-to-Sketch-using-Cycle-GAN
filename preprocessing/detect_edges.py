import cv2
import glob2
import numpy as np
from matplotlib import pyplot as plt


files=glob2.glob('png_data/*')

for i in files:
        img = cv2.imread(i,0)
        edges = cv2.Canny(img,180,255,0)
        edges = cv2.bitwise_not(edges)

        #to visualize the image
        #plt.imshow(img)
        #plt.subplot(121),plt.imshow(img,cmap = 'gray')
        #ax = plt.gca()
        #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        # plt.show()
        cv2.imwrite('edges_dataset/'+str(i.split('\\')[-1]), edges)

