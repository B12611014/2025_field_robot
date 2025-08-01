def trigger_feeder(uno):
    uno.write(b'TRIGGER\n')

def get_weight(uno):
    uno.write(b'GET_WEIGHT\n')
    data = uno.readline().decode().strip()
    return float(data) if data else 0.0

def set_led(uno, animal):
    cmd = {
        'chicken': 'LED_GREEN\n',
        'pig': 'LED_YELLOW\n',
        'cow': 'LED_RED\n'
    }.get(animal, '')
    if cmd:
        uno.write(cmd.encode())