import numpy as np
import cv2
# 이미지 파일과 컨투어의 중심값을 입력 받는다.
def match_color(img, pos):
    # 이미지 불러오기 
    image = cv2.imread("2.jpg", 1)
    # image processing
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

    # 인식할 색 입력
    colors = [[11,219,252],[0,118,255],[170,50,255],[0,0,255], [20,79,146],[0, 255, 0],[185,192,0] ,[255,0,0],[179,70,60],[203,17,186],[197,24,122],[149,149,149],[0,0,0],[255,255,255]]
    colorNames = ["yellow","orange","pink","red", "brown","green", "teal","blue","indigo","lightpurple","purple","gray","black","white"]
    
    lab = np.zeros((len(colors), 1, 3), dtype="uint8")
    for i in range(len(colors)):
        lab[i] = colors[i]

    lab = cv2.cvtColor(lab, cv2.COLOR_BGR2LAB)