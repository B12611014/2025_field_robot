# comm_mega.py
import time
from comm_imu import get_heading

def follow_line(mega, imu):
    """
    循跡移動 + IMU修正機制（簡易範例）
    這個函數可以在路線中反覆修正方向
    """
    for _ in range(30):  # 模擬跑一段時間的循跡（可根據實際狀況調整次數）
        heading = get_heading(imu)  # IMU Uno 回傳角度
        print(f"[IMU角度] {heading:.2f}°")

        if heading > 5:
            mega.write(b'LEFT\n')
        elif heading < -5:
            mega.write(b'RIGHT\n')
        else:
            mega.write(b'FORWARD\n')

        time.sleep(0.2)

    mega.write(b'STOP\n')