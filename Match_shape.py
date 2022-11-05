import cv2

def match_shape(cnt1, cnt2, contours):
    # 목표 도형에 컨투어를 얻고 컨투어를 따라 그려준다.
    path = 'shape.jpg'
    shape_contours, shape_hierarchy = return_Contour(path)

    # 모든 좌표를 작은 원으로 표시
    for contour in shape_contours:
        size = len(contour)

        # 전체 둘레의 0.05로 오차 범위 지정 --- ①
        epsilon = 0.005 * cv2.arcLength(contour, True)

        # 근사 컨투어 계산 --- ②
        approx = cv2.approxPolyDP(contour, epsilon, True)
        size = len(approx)
        img = cv2.drawContours(img, [approx], -1, (0, 0, 255), 3)
        cv2.line(img, tuple(approx[0][0]), tuple(approx[size - 1][0]), (0, 255, 0), 3)
        
        for k in range(size - 1):
            cv2.line(img, tuple(approx[k][0]), tuple(approx[k + 1][0]), (0, 255, 0), 3)

    
        center, radius = cv2.minEnclosingCircle(contour)

    
def return_Contour(img_path):
    path = img_path
    shape = cv2.imread(path)
    gray = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)    
    
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours, hierarchy


