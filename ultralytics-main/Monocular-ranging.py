from ultralytics import YOLO

# 检测：
'''model = YOLO('yolov8n.pt')
model.predict(source='ultralytics/assets', show=True, save=True)'''

# 跟踪：
'''model = YOLO('yolov8n.pt')
model.track(source='ultralytics/assets', show=True, save=True)'''

# 分割：
'''model = YOLO('yolov8n-seg.pt')
model.predict(source='ultralytics/assets', show=True, save=True)'''

# 分割+跟踪：
model = YOLO('yolov8n-seg.pt')
model.track(source='ultralytics/assets', show=True, save=True)




