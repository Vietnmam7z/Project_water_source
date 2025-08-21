import config

def relay_on():
    config.relay_pin.on()

def relay_off():
    config.relay_pin.off()

def toggle_relay():
    if config.relay_state:
        relay_on()
    else:
        relay_off()
