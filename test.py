import cv2
import numpy as np
import requests

# 함수 만들기
def web_img(url):
    image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
    image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    print(image.shape)
    cv2.imshow('Image from url', image)
    cv2.waitKey(0)

