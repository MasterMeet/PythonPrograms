import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\Xd\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

img = cv2.imread("Photo.JPG", 1)

# Reading the image as a Gray Image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Search the Co-Ordinates of the image
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.8,minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized = cv2.resize(img,(400,400))

cv2.imshow("Gray",resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()