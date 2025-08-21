import config
import uasyncio as asyncio

DEBOUNCE_DELAY = 200  # milliseconds

async def press_button():
    current = config.button_pin.value()
    if config.button_last_state == 1 and current == 0:
        config.led_pin.on()
        config.relay_state = not config.relay_state
        await asyncio.sleep_ms(DEBOUNCE_DELAY)
    elif current == 1:
        config.led_pin.off()
    config.button_last_state = current
    



