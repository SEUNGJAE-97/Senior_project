import matplotlib.pyplot as plt
import cv2
import numpy as np

target = cv2.imread('drug1.png')
shapes = cv2.imread('shape1.png')

def image_processing(image, shape):
    # target
    # 출력 할 빈 캔버스 
    output = np.zeros((image.shape[0],image.shape[1],3), np.uint8)
    # 그레이, 바이너리 스케일 변환 
    targetGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    shapesGray = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)

    targetTh = cv2.adaptiveThreshold(targetGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    shapesTh = cv2.adaptiveThreshold(shapesGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    
    # find contours 
    cntrs_target,_= cv2.findContours(targetTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
    cntrs_shapes,_= cv2.findContours(shapesTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
    
    matchs = [] # 컨투어와 매칭 점수를 보관할 리스트
    
    # thresh(1000)보다 작은 contours는 제거한다. 
    saved_contour_shapes = []
    saved_contour_target = []
    thresh = 1000
    
    for contour in cntrs_target:
        if cv2.contourArea(contour) > thresh:
            saved_contour_target.append(contour)

    for contoured in cntrs_shapes:
        if cv2.contourArea(contoured) > thresh:
            saved_contour_shapes.append(contoured)
    # 저장된 saved_contour_shapes를 output에 그린다.
    cv2.drawContours(output, saved_contour_shapes,-1,(255,255,255),1)

    for contr in cntrs_shapes:
        # 대상 도형과 여러 도형 중 하나와 매칭 실행 
        match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
        # 해당 도형의 매칭 점수와 컨투어를 쌍으로 저장 
        matchs.append( (match, contr) )
        # 해당 도형의 컨투어 시작지점에 매칭 점수 표시 
        cv2.putText(shapes, '%.2f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 0,(255,0,0),3 )
    # 매칭 점수로 정렬 
    matchs.sort(key=lambda x : x[0])
    # 가장 target에 근사한 값을 갖는 도형의 컨투어 표시
    cv2.drawContours(shapes, [matchs[0][1]],-1, (0,255,0),3)
    
    # 결과 출력
    fig = plt.figure(figsize=(10, 6))
    plt.subplot(121), plt.axis('off'), plt.imshow(output), plt.title("target")
    plt.subplot(122), plt.axis('off'), plt.imshow(shapes), plt.title("Match Shape")
    plt.show()
    

image_processing(target, shapes)
