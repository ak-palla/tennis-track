
from ultralytics import YOLO

# ## Importing a YOLO model
# model=YOLO('models/yolov8_best.py')

# ## Running it on a image 

# result = model.predict('input_videos/input_video.mp4',conf=0.2 ,save=True)
# #print(result)

# this is for tracking objects

model = YOLO('yolov8x')

result= model.track('input_videos/input_video.mp4',conf=0.2, save=True)


  


    
    
    