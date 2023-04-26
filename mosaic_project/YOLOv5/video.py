#%%
import cv2
import torch
from time import time
start_time = time()
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
#cap = cv2.VideoCapture(r'C:\Users\Administrator\Desktop\videodata\pig.mp4') # 경로상의 비디오 입력
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('pig.avi', fourcc, 25.0, (1280,  720))
#cap = cv2.VideoCapture(0)  # 기본 카메라 사용
cap = cv2.VideoCapture(r'C:\Users\Administrator\Desktop\videodata\pigman.mp4')
width = int(cap.get(3))
height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
print(width, height, fps)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('pig.mp4', fourcc, fps, (width, height))
while cap.isOpened():
    success, frame = cap.read()
    #frame = [frame]
    if success:
        output = model(frame)
        bounding_box = output.pandas().xyxy[0]
        target_class = 'person'
        num_of_target = len(bounding_box['name']==target_class)
        for i in range(num_of_target):
            x = int(bounding_box.iloc[i,0])      # x 축 시작점
            y = int(bounding_box.iloc[i,1])      # y 축 시작점
            w = int(bounding_box.iloc[i,2] - x)  # x 축 길이
            h = int(bounding_box.iloc[i,3]- y)   # y 축 길이
            sub_frame = frame[y:y+h,x:x+w]
            sub_frame = cv2.GaussianBlur(sub_frame,(0,0),1)
            frame[y:y+h,x:x+w] = sub_frame
        cv2.imshow('gaussian blur',frame)
        out.write(frame)
    else:
        
        break
    key = cv2.waitKey(1) & 0xFF
    if (key==27):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
end_time = time()
# print(end_time-start_time)
# %%

# cap = cv2.VideoCapture(r'C:\Users\Administrator\Desktop\videodata')
# width = int(cap.get(3))
# height = int(cap.get(4))
# fps = cap.get(cv2.CAP_PROP_FPS)
# print(width, height, fps)
# # out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('pig.mp4', fourcc, fps, (width, height))
# # %%
# r'C:\Users\Administrator\Desktop\videodata\pig.mp4'