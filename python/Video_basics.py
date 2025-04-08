import cv2, time
from tkinter import *

cap = cv2.VideoCapture(0)

while True:

    check,frame = cap.read()

    cv2.imshow("capturing",frame)
    
    key = cv2.waitKey(1)
    
    if (key == ord('q')):
    	break


cap.release()
cv2.destroyAllWindows()

root = Tk()
Label(root, image=frame).pack()
root.mainloop()