import cv2
import numpy as np


def loading_displaying_saving():
    img = cv2.imread('data/test2.png', 0) #cv2.IMREAD_GRAYSCALE
    np.set_printoptions(threshold=np.inf)
    dt = img[::-1, :]
    cv2.imshow('girl', dt)
    cv2.waitKey(0)
    cv2.imwrite('tt.png', dt)


loading_displaying_saving()