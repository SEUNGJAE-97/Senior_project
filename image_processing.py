import cv2
import numpy as np
# 원본 이미지로부터 앞 뒤 분리 
# 경로
#'C:\Users\hsj\Documents\GitHub\Senior_project\image'

# 00 이미지 이진화 
img = cv2.imread('aa.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

mask = 255- mask

kernel = np.ones((3,3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

result = img.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask
cv2.imshow('result',result)
cv2.waitKey()
# 01 외곽선 추출 
# 02 배경 제거 
# 03 

