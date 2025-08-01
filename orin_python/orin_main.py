# orin_main.py
import serial
import time
from vision import detect_animal
from comm_mega import follow_line
from comm_uno import trigger_feeder, get_weight, set_led


# 初始化狀態
state = 'init'
target_animal = None

# 建立與各 Arduino 通訊
mega = serial.Serial('/dev/ttyACM0', 9600)  # Arduino Mega: 馬達控制
uno = serial.Serial('/dev/ttyUSB0', 9600)   # Arduino Uno #1: 飼料觸發 + LED + 重量
imu = serial.Serial('/dev/ttyUSB1', 9600)   # Arduino Uno #2: IMU資料

# 主循環
while True:
    if state == 'init':
        print("[狀態] 等待啟動")
        time.sleep(1)
        state = 'go_to_animal_zone'

    elif state == 'go_to_animal_zone':
        print("[狀態] 前往動物辨識區")
        follow_line(mega, imu)  # 新版支援 IMU 輔助的循跡
        state = 'animal_recognition'

    elif state == 'animal_recognition':
        print("[狀態] 執行動物辨識")
        detected = detect_animal()
        if detected:
            target_animal = detected
            print(f"[辨識結果] 是 {target_animal}")
            set_led(uno, target_animal)  # UNO1亮燈
            time.sleep(2)
            state = 'go_feeder'

    elif state == 'go_feeder':
        print("[狀態] 前往飼料供應區")
        follow_line(mega, imu)
        state = 'trigger_feeder'

    elif state == 'trigger_feeder':
        print("[狀態] 觸發飼料機")
        trigger_feeder(uno)
        time.sleep(3)
        state = 'go_feed_zone'

    elif state == 'go_feed_zone':
        print("[狀態] 前往投餵區")
        follow_line(mega, imu)
        state = 'dump_feed'

    elif state == 'dump_feed':
        print("[狀態] 飼料倒入指定區域")
        set_led(uno, target_animal)  # 再次亮對應燈
        time.sleep(3)

        weight = get_weight(uno)
        print(f"[重量] 偵測為 {weight} g")
        state = 'done'

    elif state == 'done':
        print("[任務完成]")
        break