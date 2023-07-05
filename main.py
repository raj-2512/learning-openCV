import cv2

img = cv2.imread('assets/landing.jpg')


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()