import numpy as np

# 이미지 파일과 컨투어의 중심값을 입력 받는다.
def match_color(img, pos):
    x_pos, y_pos = pos
    # 추출할 색의 하한과 상한값을 정한다.
    min_color = np.array([102, 255, 255])
    max_color = np.array([102, 255, 255])

    # 빨, 주, 노, 초, 파, 흰 검
    # 코사인 유사도
    # https://doyou-study.tistory.com/49
