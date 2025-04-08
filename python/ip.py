import cv2,time

img = cv2.imread ("C:\\Users\\Abhishek A P\\Desktop\\Drone Workshop\\controller.jpg",1)

print(img.shape[1]/2)

img1 = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

#print(img1.shape)
#cv2.imwrite("C:\\Users\\Abhishek A P\\Desktop\\control.png",img)

cv2.imshow("Drone",img1)

cv2.waitKey(2000)

cv2.destroyAllWindows()
