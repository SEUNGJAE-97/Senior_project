import cv2

def find_contr(path, path2):
    # 이미지 처리 
    target= cv2.imread(path2)
    shapes = cv2.imread(path)
    shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
    targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    shapesTh = cv2.adaptiveThreshold(shapesGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    targetTh = cv2.Canny(targetGray, 150, 250)
    cv2.imshow('targetTh',targetTh)
    # 모든 컨투어 찾기 
    cntrs_shapes, hierarchy = cv2.findContours(shapesTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
    cntrs_target, hierarchy = cv2.findContours(targetTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # 노이즈 제거 
    saved_contour_target = []
    saved_contour_shapes = []
    matchs = []
    thresh_low = 100
    thresh_high = 1000

    for contoured in cntrs_shapes:
        if (cv2.contourArea(contoured) > thresh_low) & (cv2.contourArea(contoured) < thresh_high):
            saved_contour_shapes.append(contoured)
    for contour in cntrs_target:
        if (cv2.contourArea(contour) > thresh_low) :
            saved_contour_target.append(contour)
            
    for contr in saved_contour_shapes:
        match = cv2.matchShapes(saved_contour_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
        matchs.append((match,contr))
        cv2.putText(shapes, '%.2f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255),1)
    
    matchs.sort(key = lambda x : x[0])
    cv2.drawContours(shapes, [matchs[0][1]], -1, (0,255,0), 3)
    
    print(len(saved_contour_shapes))

    cv2.imshow("result", shapes)
    cv2.waitKey(0)

path2 = 'drug1.png'
path = 'shape.jpg'
find_contr(path, path2)