from ultralytics import YOLO

# 加載模型
model = YOLO('yolov8n.pt')  # 選擇您需要的 YOLOv8 模型

# 訓練模型
#model.train(data='/Users/outingan/dataset_new/data.yaml', epochs=100, imgsz=640, patience=20,device="mps")
model.train(data='/Users/outingan/dataset_new_chick_2/data_chick_2.yaml', epochs=200, imgsz=640,patience=50,augment=True,)
#model.train(data='/Users/outingan/dataset_new_bird/data_bird.yaml', epochs=150, imgsz=640)





