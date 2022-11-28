import cv2
import os
from imutils import contours

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

# 이미지 파일 이름을 불러오는 함수
def get_img_name():
    img_path_list= []
    img_name = []
    # 해당 확장자를 갖는 파일에 대해서만 for-loop 적용
    possible_img_extension = ['.jpg', '.jpeg', '.JPG', 'bmp', '.png']
    root_dir = 'C:/Users/lenovo/Documents/GitHub/Senior_project/image'
    for (root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    # 이미지를 저장할 경로 값을 갖는 img_path 
                    img_path = root + '/' + 'my_image'+'/'+file_name
                    img_path = img_path.replace('\\', '/')
                    # 이미지의 저장 경로 및 이름 값을 갖는 리스트(img_name) 
                    img_path_list.append(img_path)
                    img_name.append(file_name)
    return img_path_list, img_name 
# directory(생성할 약품의 이름값으로 생성)
def create_folder():
    img_path_list, img_name = get_img_name()
    for file in range(len(img_name)):
        path = img_path_list[file] + '/' + img_name[file]
        try : 
            if not os.path.exists(path): 
                #os.makedirs(path)
                print(path, sep='\n')
        except OSError:
            print("Error in directory ")
    

create_folder()
path = "200907150514801.JPG"
path2 = "200907150521501.JPG"
img = cv2.imread(path2)
shapesGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
shapesTh = cv2.threshold(shapesGray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# Remove horizontal lines
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
#contour 확인
#cv2.drawContours(img, detected_contours, -1 ,(0,0,255), 5) 
"""
cnt = detected_contours[0]
epsilon2 = 0.001*cv2.arcLength(cnt, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
"""
# and 연산으로 앞, 뒤 사진 따로 저장한다.
# cv2.drawContours(img, detected_contours, n ,(0,0,255), 5) 의 3번째 변수 n이 
# 1일때 첫번째 객체 컨투어를 표시 , 0 일때 두번째 객체 컨투어를 그린다.

(cnts, _) = contours.sort_contours(cnts, method="left-to-right")
num = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 1)
    original = img.copy()
    ROI = original[y:y+h, x:x+w]
    #cv2.imwrite('ROI_{}.png'.format(num), ROI)
    num += 1
    
    # while-loop  &  make folder   
    



cv2.imshow('image', img)
cv2.waitKey()

