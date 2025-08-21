import asyncio
import button
import dht11
import relay

async def task_button():
    while True:
        await button.press_button()
        await asyncio.sleep_ms(10)

async def task_relay():
    while True:
        relay.toggle_relay()
        await asyncio.sleep_ms(20)
        
async def task_dht():
    while True:
        dht11.read_dht()
        await asyncio.sleep(2)  


