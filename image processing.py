# read image from Drive
import cv2
from matplotlib import pyplot as plt

# the path of image
image_path ="D:/Image Processing Project/image/azi.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    

plt.imshow(image)
plt.axis('off') 
plt.show()


#face detection
import cv2
from matplotlib import pyplot as plt
image = cv2.imread("ai.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

model = cv2.CascadeClassifier("model.xml")
face = model.detectMultiScale(image)
print(face)

image = cv2.rectangle(image, (100,100), (200,200), (255,0,0), 3)

X = face[0][0]
y = face[0][1]
a = face[0][2]
b = face[0][3]
image = cv2.rectangle(image, (x,y), (x+a,y+b), (255,0,0), 3)












