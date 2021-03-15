# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:56:34 2021

@author: Ahmet Kasım Erbay
"""
#%% Kütüphanelerin import edilmesi
import numpy as np
import cv2
import imutils

#½½ Resmin içeri aktarılması
img_text = 'kare4.png'
img = cv2.imread(img_text)

#%% Canny'nin parametrelerinin belirlenmesi
min_value = 50
max_value = 100

#%% Canny ile kenar tespitinin yapılması
image = cv2.Canny(img, min_value, max_value) 


#%% Kontur bulma
cnts, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#%% Konturların içerisinde gezinme
for c in cnts:
    approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True) # Şeklin kenar sayısının belirlenmesi
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5) 
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
              cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
              M = cv2.moments(c)
              # Kontur merkezinin tespiti
              if M["m00"] !=0:
                    
                  cX = int(M["m10"] / M["m00"])
                  cY = int(M["m01"] / M["m00"])
                
                        # Şeklin merkezinin çizilmesi
                  cv2.circle(img, (cX, cY), 7, (0, 0, 255), -1) #(img, dairenin merkezi, merkez noktanın kalınlığı, RGB değeri)
cv2.imshow('original', img)
cv2.waitKey(0)