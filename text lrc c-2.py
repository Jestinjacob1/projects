import cv2
import matplotlib

def main():
    impath = "C:\\Users\\Lenovo\\test_folder\\python\\standard\\standard_test_images\\lena_color_256.tif"
    img=cv2.imread(impath ,1)
    
    cv2.imshow("lena",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__=="__main__":
        main()  