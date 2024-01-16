import cv2

img = cv2.imread("image/cat.jpg")

imgresize = cv2.resize(img,(700,700))

#วาดวงกลม
cv2.circle(imgresize,(100,100),30,(255,0,0),5)
#cv2.circle(imgresize,(100,100),30,(255,0,0),-1) #Fill

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()