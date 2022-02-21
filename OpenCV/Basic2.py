import cv2
import numpy as np
import time


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    #pass

def trackbars():
    # create a black image, a window
    img = np.zeros((300, 512, 3), dtype=np.uint8)
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('R', 'image', 0, 255, empty_callback)
    cv2.createTrackbar('G', 'image', 0, 255, empty_callback)
    cv2.createTrackbar('B', 'image', 0, 255, empty_callback)

    # create switch for ON/OFF functionality
    switch_trackbar_name = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch_trackbar_name, 'image', 0, 1, empty_callback)

    while True:
        cv2.imshow('image', img)

        # sleep for 10 ms waiting for user to press some key, return -1 on timeout
        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch_trackbar_name, 'image')

        if s == 0:
            # assign zeros to all pixels
            img[:] = 0
        else:
            # assign the same BGR color to all pixels
            img[:] = [b, g, r]

    # closes all windows (usually optional as the script ends anyway)
    cv2.destroyAllWindows()
def threshold():
    cv2.namedWindow('Image')
    img=cv2.imread("messi.jfif",cv2.IMREAD_GRAYSCALE)
    cv2.createTrackbar('Binary','Image',0,255,empty_callback)
    cv2.createTrackbar('Set','Image',0,4,empty_callback)
    while True:
        cv2.waitKey(10)
        pos=cv2.getTrackbarPos('Binary','Image')
        type=cv2.getTrackbarPos('Set','Image')
        if type==0:
            ret, thresh1 = cv2.threshold(img, pos, 255, cv2.THRESH_BINARY)
        if type==1:
            ret, thresh1 = cv2.threshold(img, pos, 255, cv2.THRESH_BINARY_INV)
        if type==2:
            ret, thresh1 = cv2.threshold(img, pos, 255, cv2.THRESH_TRUNC)
        if type==3:
            ret, thresh1 = cv2.threshold(img, pos, 255, cv2.THRESH_TOZERO)
        if type==4:
            ret, thresh1 = cv2.threshold(img, pos, 255, cv2.THRESH_TOZERO_INV)
        #cv2.imshow('image', img)
        cv2.imshow("Binary",thresh1)
    cv2.destroyAllWindows()
def resize():
    img=cv2.imread("qr.jpg",cv2.IMREAD_COLOR)
    img_scale=cv2.resize(img,(0,0),fx=2.5,fy=2.5)
    img_linear=cv2.resize(img,(500,500),cv2.INTER_LINEAR)
    img_nearest = cv2.resize(img, (500, 500), cv2.INTER_NEAREST)
    img_area = cv2.resize(img, (500, 500), cv2.INTER_AREA)
    img_lanczo = cv2.resize(img, (500, 500), cv2.INTER_LANCZOS4)
    cv2.imshow("INTER_LANCZOS4", img_lanczo)
    cv2.imshow("INTER_AREA", img_area)
    cv2.imshow("INTER_NEAREST", img_nearest)
    cv2.imshow("s=2.5",img_scale)
    cv2.imshow("INTER_LINEAR", img_linear)
    cv2.waitKey(0)

def blending():
    i1 = cv2.imread("qr.jpg", cv2.IMREAD_COLOR)
    i2 = cv2.imread("LOGO.jpg", cv2.IMREAD_COLOR)
    i1=cv2.resize(i1,(313,313))
    cv2.namedWindow('image')
    cv2.createTrackbar('alpha', 'image', 0, 255, empty_callback)
    while True:
        t1=time.perf_counter()
        cv2.waitKey(10)
        alpha=cv2.getTrackbarPos('alpha','image')/255.0
        beta=1.0-alpha
        dst=cv2.addWeighted(i1,alpha,i2,beta,0)
        cv2.imshow('blended',dst)
        t2=time.perf_counter()
        print((t1-t2)*1000)
def adaptative_threshold():
    img = cv2.imread('LOGO.jpg', 0)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('orginal',img)
    cv2.imshow('threshold',th2)
    cv2.waitKey(0)
    return
def negativ():
    img = cv2.imread('LOGO.jpg', cv2.IMREAD_COLOR)
    th2 = (255-img)
    cv2.imshow('orginal',img)
    cv2.imshow('negative',th2)
    cv2.waitKey(0)
    return
if __name__ == '__main__':
    negativ()