import cv2
import numpy as np
def convolution_filtering():
    img=cv2.imread("lenna_noise.bmp")
    img2 = cv2.imread("lenna_salt_and_pepper.bmp")
    kernel=np.ones((5,5),np.float32)/25
    kernel2=np.array([[0,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,0]])/21
    img_filter=cv2.filter2D(img,-1,kernel)
    img_filter2=cv2.filter2D(img,-1,kernel2)
    cv2.imshow("without filter",img)
    cv2.imshow("convolution",img_filter)
    cv2.imshow("convolution2", img_filter2)
    cv2.waitKey(0)
    return
def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    #pass
def average_filter():
    img=cv2.imread("lenna_noise.bmp")
    cv2.namedWindow('image')
    cv2.createTrackbar('box_size', 'image', 0, 10, empty_callback)
    while True:
        box=cv2.getTrackbarPos('box_size','image')
        if box%2==0:
            pos=box+1
        else:
            pos=box
        img_filter = cv2.blur(img, (pos, pos))
        cv2.imshow("without filter", img)
        cv2.imshow("Average_filter", img_filter)
        cv2.waitKey(10)
    return
def median_filter():
    img=cv2.imread("lenna_salt_and_pepper.bmp")
    img_filter=cv2.medianBlur(img,5)
    cv2.imshow("without filter", img)
    cv2.imshow("median_filter", img_filter)
    cv2.waitKey(0)
    return
def gauss_filter():
    img=cv2.imread("lenna_salt_and_pepper.bmp")
    img_filter=cv2.GaussianBlur(img,(5,5),10)
    cv2.imshow("without filter", img)
    cv2.imshow("Gauss_filter", img_filter)
    cv2.waitKey(0)
    return
def morphological_erosion():
    img = cv2.imread("j.png",cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernell=np.ones((5,5),np.uint8)
    thresh1=cv2.erode(thresh1,kernell,iterations=1)
    cv2.imshow("without erosion", img)
    cv2.imshow("with erosion", thresh1)
    cv2.waitKey(0)
def morphological_dilation():
    img = cv2.imread("j.png",cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernell=np.ones((5,5),np.uint8)
    thresh1=cv2.dilate(thresh1,kernell,iterations=1)
    cv2.imshow("without dilation", img)
    cv2.imshow("with dilation", thresh1)
    cv2.waitKey(0)
def morphological_open():
    img = cv2.imread("lenna_salt_and_pepper.bmp",cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernell=np.ones((5,5),np.uint8)
    thresh1=cv2.morphologyEx(thresh1,cv2.MORPH_OPEN,kernell)
    cv2.imshow("without Open", img)
    cv2.imshow("with Open", thresh1)
    cv2.waitKey(0)
def morphological_close():
    img = cv2.imread("lenna_salt_and_pepper.bmp",cv2.IMREAD_GRAYSCALE)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernell=np.ones((2,2),np.uint8)
    thresh1=cv2.morphologyEx(thresh1,cv2.MORPH_CLOSE,kernell)
    cv2.imshow("without Open", img)
    cv2.imshow("with Open", thresh1)
    cv2.waitKey(0)
def white_pix():
    img=cv2.imread("messi.jfif",cv2.IMREAD_GRAYSCALE)
    x,y=np.shape(img)
    for i in range(x):
        for j in range(y):
            if i%3==0 and j%3==0:
                img[i,j]=255
    cv2.imshow("Messi",img)
    cv2.waitKey(0)
def my_filtr():
    np.seterr(over='ignore')
    img = cv2.imread("lenna_noise.bmp", cv2.IMREAD_GRAYSCALE)
    x,y=np.shape(img)
    for i in range(x):
        for j in range(y):
            if (i==0 or j==0 or i==x-1 or j==y-1):
                img[i,j]=img[i,j]
            else:
                img[i,j]=np.sum(img[(j-1):(j+1), (i-1):(i+1)])/9
    cv2.borderInterpolate(y,x,cv2.BORDER_CONSTANT)
    cv2.imshow("Lenna", img)
    cv2.waitKey(0)
def Kuwahara_filter(a):
    img=cv2.imread("lenna_noise.bmp",cv2.IMREAD_GRAYSCALE)
    x,y=np.shape(img)
    for i in range(x):
        for j in range(y):
            if (i<a or j<a or i>x-a-1 or j>y-a-1):
                img[i,j]=img[i,j]
            else:
                mean_a, std_a=cv2.meanStdDev(img[(j-a):(j-1),(i-a):(i-1)])
                mean_b, std_b = cv2.meanStdDev(img[(j - a):(j - 1), (i + 1):(i + a)])
                mean_c, std_c = cv2.meanStdDev(img[(j + 1):(j + a), (i - a):(i - 1)])
                mean_d, std_d = cv2.meanStdDev(img[(j + 1):(j + a), (i + 1):(i + a)])
                min_mean=min([std_a,std_b,std_c,std_d])
                if min_mean==mean_a:
                    img[i,j]=int(std_a)
                elif min_mean == mean_b:
                    img[i, j] = int(std_b)
                elif min_mean == mean_c:
                    img[i, j] = int(std_c)
                else:
                    img[i, j] = int(std_d)
    cv2.imshow("Lenna", img)
    cv2.waitKey(0)
if __name__ == '__main__':
  Kuwahara_filter(2)