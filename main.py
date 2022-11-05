import cv2
import Match_color
import Match_shape

# 파일을 흑백으로 불러온다.
f_path = 'drug1.png'
img = cv2.imread(f_path, cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 블러처리
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

# 캐니 엣지 검출, 모양을 검출한다.
edges = cv2.Canny(blurred_img, 100, 200)
# th3 = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)

# 컨투어 
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#1 여러 도형 중 매칭점수가 제일 높은것을 선별 (cv2.matchShapes())
# 참고링크)https://bkshin.tistory.com/entry/OpenCV-22-%EC%BB%A8%ED%88%AC%EC%96%B4Contour
    
Match_shape.match_shape(cnt1, cnt2)

#2 center 지점의 색을 매칭하기
Match_color.match_color(img, center)

cv2.imshow('result', img)
cv2.waitKey()
