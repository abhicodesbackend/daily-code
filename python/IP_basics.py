import cv2,time

def m():
    
    img = cv2.imread ('D://Desktop_files//CT-2 GUI project 2020//bms.png',1)
    print(img.shape)

    img1 = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
    #print(img1.shape)
    #cv2.imwrite("C:\\Users\\Abhishek A P\\Desktop\\control.png",img)

    cv2.imshow("Drone",img1)
    print(img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    m()

