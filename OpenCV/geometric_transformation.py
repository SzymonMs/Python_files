import cv2
import numpy as np
import matplotlib.pyplot as plt
def mouse_drawing():
    # mouse callback function
    def draw(event, x, y, flags, param):
        if event == cv2.EVENT_RBUTTONDBLCLK:
            cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        elif event==cv2.EVENT_LBUTTONDBLCLK:
            cv2.rectangle(img,(x,y),(x+50,y+40),(0,255,0),thickness=2)
    # Create a black image, a window and bind the function to window
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw)
    while (1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    return
def perspective():
    img=cv2.imread("road.jpg")
    img_linear=cv2.resize(img,(500,500),cv2.INTER_LINEAR)
    cv2.namedWindow('test')
    rows, cols, ch = img.shape
    print(img.shape)
    data_x=[]
    data_y=[]
    ''''TO DO'''
    def draw(event, x, y, flags, param):
        if event==cv2.EVENT_LBUTTONDBLCLK:
                data_x.append(x)
                data_y.append(y)
        pts1 = np.float32(
            [[data_x[0], data_y[0]], [data_x[1], data_y[1]], [data_x[2], data_y[2]], [data_x[3], data_y[3]]])
        pts2 = np.float32(
            [[data_x[0], data_y[0]], [data_x[1], data_y[1]], [data_x[0], data_y[2]], [data_x[1], data_y[3]]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (500, 500))
        cv2.imshow('test2', dst)
    cv2.imshow('test',img_linear)
    cv2.setMouseCallback('test', draw)
    cv2.waitKey(0)
def histogram():
    img = cv2.imread('messi.jfif', 0)
    plt.hist(img.ravel(), 256, [0, 256]);
    plt.show()
    img = cv2.imread('messi.jfif')
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()
def thresh_part_of_image():
    img = cv2.imread('messi.jfif',0)
    data_x=[]
    data_y=[]
    cv2.namedWindow('window')
    def draw(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            data_x.append(x)
            data_y.append(y)
        im=img[data_y[0]:data_y[1],data_x[0]:data_x[1]]
        ret, thresh1 = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
        img[data_y[0]:data_y[1], data_x[0]:data_x[1]]=thresh1
        cv2.imshow('window',img)

    cv2.imshow('window',img)
    cv2.setMouseCallback('window', draw)
    cv2.waitKey(0)
i=0
j=0
def write_txt_and_draw():
    # mouse callback function
    def draw(event, x, y, flags, param):
        if event == cv2.EVENT_RBUTTONDBLCLK:
                cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
                global i
                i=i+1
                cv2.putText(img,str(i),(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))

        elif event==cv2.EVENT_LBUTTONDBLCLK:
                cv2.rectangle(img,(x,y),(x+50,y+40),(0,255,0),thickness=2)
                global j
                j=j+1
                cv2.putText(img, str(j), (x -10, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255))
    # Create a black image, a window and bind the function to window
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    while (1):
        cv2.setMouseCallback('image', draw)
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
##TO DO
def mops():
    img2 = cv2.imread("gallery.png")
    data_x=[]
    data_y=[]
    def draw(event, x, y, flags, param):
        i=0
        img1 = cv2.imread("pug.png")
        if event==cv2.EVENT_LBUTTONDBLCLK:
                data_x.append(x)
                data_y.append(y)

        img1 = cv2.resize(img1, (abs(data_x[1] - data_x[0]), abs(data_y[0] - data_y[1])))
        img2[data_y[0]:data_y[1], data_x[0]:data_x[1]]=img1
        cv2.imshow('Gallery',img2)
    cv2.imshow('Gallery',img2)
    cv2.setMouseCallback('Gallery',draw)
    cv2.waitKey(0)
if __name__ == '__main__':
    mops()