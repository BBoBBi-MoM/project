#%%
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
#%%
import cv2
import pandas as pd
#%% normal mosaic
file = 'kju.jpg'
img = cv2.imread(file)
print(type(img))
result = model(img)
detection_info = result.pandas().xyxy[0]
target_class = 'person'
rate = 15
num_of_target = len(detection_info[detection_info['name']==target_class])
for i in range(num_of_target):
    x = int(detection_info.iloc[i,0])      # x 축 시작점
    y = int(detection_info.iloc[i,1])      # y 축 시작점
    w = int(detection_info.iloc[i,2] - x)  # x 축 길이
    h = int(detection_info.iloc[i,3]- y)  # y 축 길이
    sub_img = img[ y:y+h , x:x+w]
    sub_img = cv2.resize(sub_img,(w//rate,h//rate))
    sub_img = cv2.resize(sub_img,(w,h))
    img[y:y+h,x:x+w] = sub_img

cv2.imshow('img',img)
cv2.imwrite(f'./mosaic_{file}',img)
cv2.waitKey(0)
# %% gaussian blur
file = 'kju.jpg'
img = cv2.imread(file)
result = model(img)
detection_info = result.pandas().xyxy[0]
target_class = 'person'
num_of_target = len(detection_info[detection_info['name']==target_class])
for i in range(num_of_target):
    x = int(detection_info.iloc[i,0])      # x 축 시작점
    y = int(detection_info.iloc[i,1])      # y 축 시작점
    w = int(detection_info.iloc[i,2] - x)  # x 축 길이
    h = int(detection_info.iloc[i,3]- y)  # y 축 길이
    sub_img = img[ y:y+h , x:x+w]
    sub_img = cv2.GaussianBlur(sub_img,(0,0),7)
    img[y:y+h, x:x+w] = sub_img
cv2.imshow('img',img)
cv2.imwrite(f'./gaussian_blur_{file}',img)
cv2.waitKey(0)

# %%
