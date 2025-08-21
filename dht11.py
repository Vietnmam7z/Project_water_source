import config

def read_dht():
    try:
        config.sensor.measure()
        config.temperature = config.sensor.temperature()
        config.humidity = config.sensor.humidity()
        return config.temperature, config.humidity
    except Exception as e:
        print("Lỗi đọc cảm biến:", e)
