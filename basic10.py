import cv2

img = cv2.imread("image/cat.jpg")

imgresize = cv2.resize(img,(700,700))

#วาดเส้นตรง
cv2.line(imgresize,(100,100),(500,200),(255,0,0),5)
cv2.arrowedLine(imgresize,(300,300),(600,300),(255,255,0),5)

cv2.imshow("Output_line", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()