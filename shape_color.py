import cv2
import math 

def find_contr(path, path2):
    # 이미지 처리 
    target= cv2.imread(path2)
    shapes = cv2.imread(path)
    shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
    targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    shapesTh = cv2.adaptiveThreshold(shapesGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    targetTh = cv2.Canny(targetGray, 150, 250)
    
    # 모든 컨투어 찾기 
    cntrs_shapes, hierarchy = cv2.findContours(shapesTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
    cntrs_target, hierarchy = cv2.findContours(targetTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    # 노이즈 제거 
    saved_contour_shapes = []
    matchs = []
    thresh_low = 100
    thresh_high = 1000

    for contoured in cntrs_shapes:
        if (cv2.contourArea(contoured) > thresh_low) & (cv2.contourArea(contoured) < thresh_high):
            saved_contour_shapes.append(contoured)
    
    """
    # 제거 
    for contour in cntrs_target:
        if (cv2.contourArea(contour) > 50) :
            saved_contour_target.append(contour)
    """
    
    for contr in saved_contour_shapes:
        match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
        matchs.append((match,contr))
        cv2.putText(shapes, '%.2f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255),1)
    
    matchs.sort(key = lambda x : x[0])
    cv2.drawContours(shapes, [matchs[0][1]], -1, (0,255,0), 3)
    cv2.imshow("result", shapes)
    
    cx, cy = find_center(cntrs_target)
    center = (cx, cy)
    color = match_color(target, center)
    print(color)
    cv2.waitKey(0)


def match_color(img, contours):
    # 0. 인식할 색상 RGB값 
    colors = [[11,219,252],[0,118,255],[170,50,255],[0,0,255], [20,79,146],[0, 255, 0],[185,192,0] ,[255,0,0],[179,70,60],[203,17,186],[197,24,122],[149,149,149],[0,0,0],[255,255,255]]
    colorNames = ["yellow","orange","pink","red", "brown","green", "teal","blue","indigo","lightpurple","purple","gray","black","white"]
    cx, cy = map(int, contours)
    (b,g,r) = img[cy, cx]
    color = (r, g, b)
    for i in range(len(colors)):
        if i == 0 :
            min = dst(color, colors[i])
            c = i
        elif min > dst(color, colors[i]):
            min = dst(color, colors[i])
            c = i
        
    print("b: {0} , g : {1}, r : {2}".format(b,g,r))
    return colorNames[i]
    

# 색상의 유사도 (distance = √ ((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2))
def dst(x,y):
    total = 0
    for i in range(0,len(x)):
        a = (abs(x[i]-y[i]))**2
        total += a
    return math.sqrt(total)

def find_center(contours):
    cnt = contours[0]
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    return cx, cy


path2 = 'drug1.png'
path = 'shape.jpg'
find_contr(path, path2)

