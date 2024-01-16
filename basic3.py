#change image size
import cv2

img = cv2.imread("image/cat.jpg", -1)
imgresize = cv2.resize(img,(400,400))

cv2.imshow("output", imgresize)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()