from ultralytics import YOLO
import cv2

# 載入你訓練好的模型
model = YOLO('runs/detect/train4/weights/best.pt')  # 使用訓練好的模型權重

# 設置置信度閾值
confidence_threshold = 0.1  # 可以根據需要調整這個值

# 打開攝像頭
cap = cv2.VideoCapture(0)  # 0 代表默認攝像頭，你也可以改成其他數字來選擇不同的攝像頭

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 使用模型進行推理
    results = model(frame)

    # 顯示結果
    for result in results:
        boxes = result.boxes
        print(f'Detected {len(boxes)} objects')
        for box in boxes:
            # 將張量轉換為標量
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            label = model.names[int(box.cls.item())]
            confidence = box.conf.item()

            # 只顯示置信度高於閾值的邊界框
            if confidence >= confidence_threshold:
                # 在圖片上繪製矩形框和標籤
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # 使用 OpenCV 顯示圖片
    cv2.imshow('Result', frame)

    # 按 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝像頭並關閉所有 OpenCV 視窗
cap.release()
cv2.destroyAllWindows()
