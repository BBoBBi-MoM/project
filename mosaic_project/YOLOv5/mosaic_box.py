#%%
import cv2 as cv
import numpy as np

img = cv.imread('dprk.jpg')
img_copy = img.copy()
empty_img = np.zeros_like(img)  # 이미지랑 같은 크기의 빈 배열 생성

# [x1, y1, x2, y2]
boxes = [[100, 100, 350, 500], [200, 50, 550, 250], [300, 400, 600, 650], [490, 100, 700, 600]]
boxes = np.array(boxes)

for box in boxes:
    img_ = cv.rectangle(img_copy, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), -1)  # 네모박스 치세용
    empty_ = cv.rectangle(empty_img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 1)  # 네모박스 치세용
    
cv.imshow('img', img_)  # 박스 겹친 부분
cv.imshow('empty_img', empty_)  # 빈 이미지에 박스 친거
cv.waitKey(-1)
#%%
# 겹친 부분 최소 최대값 구하기
box_min_x, box_min_y = boxes[:, :2].min(axis=0)
box_max_x, box_max_y = boxes[:, 2:].max(axis=0)
print(box_min_x, box_min_y)
print(box_max_x, box_max_y)

img_bbox = img[box_min_y: box_max_y, box_min_x: box_max_x, :]  # 이미지에서 박스 최소 ~ 최대 부분만 잘라내기
empty_img_bbox = empty_img[box_min_y: box_max_y, box_min_x: box_max_x, :]  # 빈 이미지에서 박스 최소 ~ 최대 부분만 잘라내기
is_boxed = (empty_img_bbox > 0)

# 모자이크
h, w, c = img_bbox.shape
resized_img = cv.resize(img_bbox, (50, 50))
mosaic_img = cv.resize(resized_img, (w, h))

# img_bbox[is_boxed] = mosaic_img
final_img = np.where(is_boxed, mosaic_img, img_bbox)  # 네모 친 부분에만 모자이크

img[box_min_y: box_max_y, box_min_x: box_max_x, :] = final_img  # 전체 이미지에 모자이크 처리된 이미지 넣기

cv.imshow('img_bbox', img_bbox)  # 박스 겹친 부분
cv.imshow('empty_img_bbox', empty_img_bbox)  # 빈 이미지 박스 겹친 부분
cv.imshow('mosaic', mosaic_img)  # 모자이크 처리 된거
cv.imshow('final_img', img)  # 최종 결과물
cv.waitKey(-1)   
# %%
