import numpy as np
import cv2
import math
def match_color(img, contours):

    # 인식할 색 입력
    # blue, green, red
    colors = [[11,219,252],[0,118,255],[170,50,255],[0,0,255], [20,79,146],[0, 255, 0],[185,192,0] ,[255,0,0],[179,70,60],[203,17,186],[197,24,122],[149,149,149],[0,0,0],[255,255,255]]
    colorNames = ["yellow","orange","pink","red", "brown","green", "teal","blue","indigo","lightpurple","purple","gray","black","white"]
    
    # image processing
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
    
    # 색검출할 색공간으로 LAB사용
    blank = np.zeros(thresh.shape[:2], dtype='uint8')
    cv2.drawContours(blank, contours, -1, (255,0,0),1)

    # 이미지 중심점 찾기
    for i in contours:
        M = cv2.moments(i)
        if M['m00']!=0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
            cv2.circle(img, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        print(f"x: {cx} y: {cy}")
    
    # 좌표에 해당하는 RGB 값 받아오기
    (b,g,r) = img[cx, cy]
    print("b: {0} , g : {1}, r : {2}".format(b,g,r))
    


# 목표 좌표와 얻은 좌표값 간의 거리를 반환한다.
def dst(x,y):
    for i in range(0,len(x)):
        a = (abs(x[i]-y[i]))**2
        total += a
    return math.sqrt(total)
        


# 이미지 불러오기 
path = "drug2.jpg"
image = cv2.imread("drug2.jpg", 1)
contours = return_Contour(path)
print(contours)



