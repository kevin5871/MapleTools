"""
import requests
from bs4 import BeautifulSoup as bs

item = '마스터리 북 30'
world = '스카니아'
page = requests.get(url='https://maple.market/items/%s/%s'%(item, world))
soup = bs(page.text, 'html.parser')
divTag = soup.find_all("div", {"class": "auction-list"})
print(divTag)
for tag in divTag:
    tdTags = tag.find_all("td")
    for tag in tdTags:
        print(tag.text)
"""
#https://namu.wiki/w/%EB%A9%94%EC%9D%B4%ED%94%8C%EC%8A%A4%ED%86%A0%EB%A6%AC/%EC%8B%9C%EC%8A%A4%ED%85%9C/%EA%B2%BD%ED%97%98%EC%B9%98

import cv2
import numpy as np

img = cv2.imread('Untitled.jpg', cv2.IMREAD_UNCHANGED)

#convert img to grey
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#set a thresh
thresh = 250
#get threshold image
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
#find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#create an empty image for contours
img_contours = np.zeros(img.shape)
# draw the contours on the empty image
cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
#save image
cv2.imwrite('contours.png',img_contours)