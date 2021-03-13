import cv2
img = cv2.imread("Photo.JPG",1)
Resize_Img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("450X450",Resize_Img)
cv2.waitKey()
cv2.destroyAllWindows()