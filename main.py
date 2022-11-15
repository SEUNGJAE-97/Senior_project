import cv2


path = 'drug.PNG'
target = cv2.imread(path)
targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
targetTh = cv2.adaptiveThreshold(targetGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)

cntrs_shapes, hierarchy = cv2.findContours(targetTh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

saved_contour_shapes = []
thresh_low = 500
thresh_high = 1000

for contoured in cntrs_shapes:
        if (cv2.contourArea(contoured) > thresh_low) & (cv2.contourArea(contoured) < thresh_high):
            saved_contour_shapes.append(contoured)

cv2.drawContours(target, saved_contour_shapes, -1, (255,255,0), 3)
cv2.imshow('target',target)
cv2.waitKey(0)