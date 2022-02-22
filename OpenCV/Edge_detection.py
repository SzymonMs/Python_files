import cv2
import numpy as np
import matplotlib.pyplot as plt
##TO DO Prewitt and SOBEL, bo to nie jest dobre
def Prewitt_mask():
    img=cv2.imread("LOGO.jpg",0)
    kernel_x=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    img_filter_x = cv2.filter2D(img, -1, kernel_x)/3
    img_filter_y = cv2.filter2D(img, -1, kernel_y) / 3
    cv2.imshow("normal",img)
    cv2.imshow("edge",img_filter_x)
    cv2.imshow("edgey", img_filter_y)
    cv2.waitKey(0)
def Sobel_mask():
    img=cv2.imread("rocket.jpg",0)
    kernel_x=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, 1]])
    img_filter = cv2.filter2D(img, -1, kernel_x)/4
    img_filter_y = cv2.filter2D(img, -1, kernel_y) / 4
    cv2.imshow("normal",img)
    cv2.imshow("edge",img_filter)
    cv2.imshow("edgey", img_filter_y)
    cv2.waitKey(0)
def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    #pass

def Canny():
    img=cv2.imread("messi.jfif",0)
    cv2.namedWindow('Image')
    cv2.createTrackbar('th1', 'Image', 100, 1000, empty_callback)
    cv2.createTrackbar('th2', 'Image', 100, 1000, empty_callback)
    while True:
        th1=cv2.getTrackbarPos('th1','Image')
        th2 = cv2.getTrackbarPos('th2', 'Image')
        img1=cv2.Canny(img,th1,th2)
        cv2.imshow("w",img)
        cv2.imshow("a",img1)
        cv2.waitKey(10)
def line_and_circ():
    img=cv2.imread("shapes.jpg",0)
    x,y=img.shape
    img=cv2.resize(img,(x-100,y-100))
    edges=cv2.Canny(img,200,400,apertureSize=3)
    ##TO DO- DOBRAĆ JAKIEŚ FAJNE WSPÓŁCZYNNIKI
    lines=cv2.HoughLines(edges,1,np.pi/180,140) #zmniejszanie ostatnie parametru --> więcej linii
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 700,param1=10,param2=30,minRadius=0,maxRadius=60)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('line',img)
    cv2.waitKey(0)
def space_ship_edgde():
    img=cv2.imread("drone_ship.jpg",0)
    edges = cv2.Canny(img, 200, 900, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 120)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('line',img)
    cv2.waitKey(0)

if __name__ == '__main__':
    Canny()