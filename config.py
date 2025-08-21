from machine import Pin
import dht

# Wifi
SSID = ""
PASSWORD = ""

# Relay
relay_pin = Pin(32, Pin.OUT)

# Button
button_pin = Pin(27, Pin.IN, Pin.PULL_UP)
button_state = False

# LED
led_pin = Pin(2, Pin.OUT)

# Trạng thái relay
relay_state = False

# Trạng thái nút trước đó
button_last_state = 1

# Biến lưu nhiệt độ và độ ẩm
sensor = dht.DHT11(Pin(26))
temperature = None
humidity = None
