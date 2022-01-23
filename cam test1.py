import cv2
import matplotlib.pyplot as plt
import numpy

def main():
    cap= cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame= cap.read()
        print(ret)
        print(frame)
    else:
        ret=False
    img1= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(img1)
    plt.title("vaaaaaaa")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    cap.release()
    
    
    cv2.imshow("w",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
        main()