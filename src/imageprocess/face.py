import cv2
  
# Read the input image
img = cv2.imread('sample/ali.png')
# cv2.imshow("Original", img)
print(type(img))

# face_cascade = cv2.CascadeClassifier('src/etc/haarcascade_frontalface_alt2.xml')
    
# # Detect faces
# faces = face_cascade.detectMultiScale(img, 1.1, 4)

# # Draw rectangle around the faces and crop the faces
# for (x, y, w, h) in faces:
#     faces = img[y:y + h, x:x + w]
#     faces = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)

# if(type(faces)==type(img)):
#     print("yes")
# # Convert into grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)  
# # Load the cascade
# face_cascade = cv2.CascadeClassifier('src/etc/haarcascade_frontalface_alt2.xml')
  
# # Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  
# # Draw rectangle around the faces and crop the faces
# for (x, y, w, h) in faces:
#     # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
#     faces = img[y:y + h, x:x + w]
#     cv2.imshow("face",faces)
#     cv2.imwrite('face.jpg', faces)
      
# # Display the output
# cv2.imwrite('detcted.jpg', img)
# cv2.imshow('img', img)
# cv2.waitKey()