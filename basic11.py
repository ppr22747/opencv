import cv2

img = cv2.imread("image/cat.jpg")

imgresize = cv2.resize(img,(700,700))

#วาดสี่เหลี่ยม
cv2.rectangle(imgresize,(100,100),(500,200),(255,0,0),5)
#cv2.rectangle(imgresize,(100,100),(500,200),(255,0,0),-1) #Fill

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()