import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread('drug1.png')
shape = cv2.imread('shape1.png')

def image_processing(image, shape):
    # target
    output = np.zeros((image.shape[0],image.shape[1],3), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 

    # shapes
    output_shape = np.zeros((shape.shape[0],shape.shape[1],3), np.uint8)
    gray_shape = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
    threshold_shape = cv2.adaptiveThreshold(gray_shape, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    contours_shape, hierarchy = cv2.findContours(threshold_shape,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 

    saved_contour_shape = []
    saved_cont = []
    thresh = 1000

    for contour in contours:
        if cv2.contourArea(contour) > thresh:
            print(cv2.contourArea(contour))
            saved_cont.append(contour)

    cv2.drawContours(output, saved_cont,-1,(255,255,255),1)

    for contoured in contours_shape:
        if cv2.contourArea(contoured) > thresh:
            print(cv2.contourArea(contoured))
            saved_contour_shape.append(contoured)

    cv2.drawContours(output_shape, saved_cont,-1,(255,255,255),1)

    # ---------------------------------
    matchs = [] # 컨투어와 매칭 점수를 보관할 리스트
    for contr in contours_shape:
    # 대상 도형과 여러 도형 중 하나와 매칭 실행 
        match = cv2.matchShapes(contours_shape[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
    # 해당 도형의 매칭 점수와 컨투어를 쌍으로 저장 
        matchs.append( (match, contr) )
    # 해당 도형의 컨투어 시작지점에 매칭 점수 표시 
        #cv2.putText(shapes, '%.2f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 7,(255,0,0),3 )
    # 매칭 점수로 정렬 
    
    matchs.sort(key=lambda x : x[0])
    
    # 결과 출력
    fig = plt.figure(figsize=(10, 6))
    plt.subplot(121), plt.axis('off'), plt.imshow(output), plt.title("target")
    plt.subplot(122), plt.axis('off'), plt.imshow(output_shape), plt.title("Match Shape")
    plt.show()
    

image_processing(image, shape)
