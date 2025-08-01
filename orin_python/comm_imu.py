# comm_imu.py
def get_heading(imu_serial):
    imu_serial.write(b'GET_HEADING\n')
    response = imu_serial.readline().decode().strip()
    try:
        heading = float(response)
    except:
        heading = 0.0
    return heading