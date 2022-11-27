import cv2
import matplotlib as plt
import numpy as np
def moment(image):
    contours = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[0]
    cv2.drawContours(image, [cnt], 0, (255,255,0),1)
    #epsilon1 = 0.01 * cv2.arcLength(cnt, True)
    epsilon2 = 0.1 * cv2.arcLength(cnt, True)

    #approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

    cv2.drawContours(image, [approx2], 0, (0,255,0), 3)
    cv2.imshow(image)
    return image



path = "200907150514801.JPG"
path2 = "200907150521501.JPG"
img = cv2.imread(path)
shapesGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
shapesTh = cv2.threshold(shapesGray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

horizontal_kernel  = cv2.getStructuringElement(cv2.MORPH_RECT, (10,3))
detected_lines = cv2.morphologyEx(shapesTh, cv2.MORPH_OPEN, horizontal_kernel, iterations= 2)

cntrs_shapes = cv2.findContours(detected_lines,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cntrs_shapes = cntrs_shapes[0] if len(cntrs_shapes) == 2 else cntrs_shapes[1]
for c in cntrs_shapes:
    cv2.drawContours(detected_lines, [c], -1, (255,255,255), 5)

# Remove vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,10))
remove_vertical = cv2.morphologyEx(shapesTh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    result = cv2.drawContours(detected_lines , [c], -1, (255,255,255), 5)


detected_contours,_ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, detected_contours, -1 ,(0,0,255), 5) 
"""
cnt = detected_contours[0]
epsilon2 = 0.001*cv2.arcLength(cnt, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
"""
# for-loop으로 앞, 뒤 사진 따로 저장할것.
# cv2.drawContours(img, detected_contours, n ,(0,0,255), 5) 의 3번째 변수 n이 
# 1일때 첫번째 객체 컨투어를 표시 , 0 일때 두번째 객체 컨투어를 그린다.
for c in cnts:
    mask = np.zeros(detected_lines.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
  
    # show the images
    #cv2.imshow("Image", img)
    #cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(img, img, mask=mask))
    cv2.waitKey(0)





#cv2.imshow('result', mask)
#cv2.waitKey()



