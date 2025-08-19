from ultralytics import YOLO

# 加載模型
model = YOLO('/content/2025_field_robot/yolov8n.pt')  # 選擇您需要的 YOLOv8 模型

# 訓練模型

model.train(data='/content/2025_field_robot/dataset/data.yaml', epochs=200, imgsz=640,patience=50,augment=True,)






