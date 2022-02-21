import cv2
import matplotlib.pyplot as plt
import numpy as np
import keyboard

#cv2.imread- wczytanie obrzu
#cv2.imwrite- zapisanie obrazu do pliku
#cv2.imshow- wyświetlenie obrazka
#cv2.waitKey(0)- czekanie na zamkniecie okna obrazu
#cv2.split()- podzial na składowe
def camera_test():
    cap=cv2.VideoCapture(0)
    key=ord('a')
    while key!=ord('q'):
        ret,frame=cap.read()
        img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        img_filtered=cv2.GaussianBlur(img_gray,(7,7),1.5)
        img_edges=cv2.Canny(img_filtered,0,30,3)
        cv2.imshow('result',img_edges)
        key=cv2.waitKey(30)
    cap.release()
    cv2.destroyAllWindows()
def photo():
    img=cv2.imread("rocket.jpg",cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("rcoket2.jpg",img)
    cv2.imshow("Rocket", img)
    img2 = cv2.imread("rocket.jpg",cv2.IMREAD_COLOR)
    cv2.waitKey(0)
    print(np.shape(img2))
    print(img.shape)
def pixel_brightness():
    img = cv2.imread("rocket.jpg", cv2.IMREAD_GRAYSCALE)
    px=img[220,270]
    print(f' Pixel value at [220,270]: {px}')
    img = cv2.imread("rocket.jpg", cv2.IMREAD_COLOR)
    px = img[220, 270]
    print(f' Pixel value at [220,270]: {px}')
def cut_ROI():
    img=cv2.imread("messi.jfif",cv2.IMREAD_COLOR)
    ball=img[156:182,170:198]
    img[156:182,43:71]=ball
    cv2.imshow("Messi",img)
    cv2.waitKey(0)
def show_picture():
    img=cv2.imread("messi.jfif",cv2.IMREAD_COLOR)
    cv2.imshow("Messi",img)
    plt.imshow(img)
    plt.show()
    cv2.waitKey(0)
def split_picture():
    img=cv2.imread("AdditiveColor.png",cv2.IMREAD_COLOR)
    b,g,r=cv2.split(img)
    cv2.imshow("Blue",b)
    cv2.waitKey(0)
    cv2.imshow("Green", g)
    cv2.waitKey(0)
    cv2.imshow("Red", r)
    cv2.waitKey(0)
def camera_frame():
    cap=cv2.VideoCapture(0)
    key=ord('a')
    while key != ord('q'):
        img_gray=0
        if keyboard.is_pressed("space"):
            ret, frame = cap.read()
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('result', img_gray)
        key = cv2.waitKey(30)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_frame()