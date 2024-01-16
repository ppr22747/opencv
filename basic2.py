#image display
import cv2

img = cv2.imread("image/cat.jpg")
cv2.imshow("output", img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()