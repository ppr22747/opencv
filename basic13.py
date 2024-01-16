import cv2

img = cv2.imread("image/cat.jpg")

imgresize = cv2.resize(img,(700,700))

#วาดข้อความบนภาพ
# putText(ภาพ, ข้อความ, พิกัด (x,y), font, ขนาดข้อความ, สี, stroke)
cv2.putText(imgresize,'CAT',(100,600),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,255),cv2.LINE_AA)

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()