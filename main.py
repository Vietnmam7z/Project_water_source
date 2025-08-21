import uasyncio as asyncio
import task
from micropyserver import MicroPyServer
import utils
from wifi_connect import start_wifi
import _thread
import socket
import uselect
import config

server = MicroPyServer(port=80)
start_wifi(config.SSID,config.PASSWORD)

async def main():
    asyncio.create_task(task.task_button())
    asyncio.create_task(task.task_relay())
    asyncio.create_task(task.task_dht())
    while True:
        await asyncio.sleep_ms(10)
    
def home(request):
    try:
        with open("home.html") as f:
            html = f.read()
        server.send("HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html)
    except:
        server.send("HTTP/1.0 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nKhông thể tải giao diện.")
        
def home_css(request):
    try:
        with open("home.css") as f:
            css = f.read()
        server.send("HTTP/1.0 200 OK\r\nContent-Type: text/css\r\n\r\n" + css)
    except:
        server.send("HTTP/1.0 404 Not Found\r\nContent-Type: text/plain\r\n\r\nKhông tìm thấy file CSS.")
        
def home_js(request):
    with open("home.js") as f:
        js = f.read()
    server.send("HTTP/1.0 200 OK\r\nContent-Type: application/javascript\r\n\r\n" + js)

def toggle_relay_web(request):
    try:
        config.relay_state = not config.relay_state  # Đảo trạng thái
        server.send("HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\nRelay toggled")
    except:
        server.send("HTTP/1.0 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nLỗi khi xử lý relay.")

def sensor_web(request):
    try:
        # Giả sử giá trị đã được cập nhật ở nơi khác
        temperature = config.temperature
        humidity = config.humidity

        if temperature is None or humidity is None:
            raise ValueError("Sensor data not available")

        response = (
            "HTTP/1.0 200 OK\r\n"
            "Content-Type: application/json\r\n\r\n"
            f'{{"temperature": {round(temperature, 1)}, "humidity": {round(humidity, 1)}}}'
        )
        server.send(response)

    except Exception as e:
        error_response = (
            "HTTP/1.0 500 Internal Server Error\r\n"
            "Content-Type: application/json\r\n\r\n"
            f'{{"error": "{str(e)}"}}'
        )
        server.send(error_response)

def status_web(request):
    try:
        state = config.relay_state
        response = (
            "HTTP/1.0 200 OK\r\n"
            "Content-Type: application/json\r\n\r\n"
            f'{{"relay_state": {str(state).lower()}}}'
        )
        server.send(response)
    except Exception as e:
        server.send(
            "HTTP/1.0 500 Internal Server Error\r\n"
            "Content-Type: application/json\r\n\r\n"
            f'{{"error": "{str(e)}"}}'
        )
        
def run_server():
    try:
        server.start()
    except Exception as e:
        print("Lỗi server:", e)
        

_thread.start_new_thread(run_server, ())
server.add_route("/", home)
server.add_route("/home.css", home_css)
server.add_route("/home.js", home_js)
server.add_route("/toggle", toggle_relay_web)
server.add_route("/sensor", sensor_web)
server.add_route("/status", status_web)

asyncio.run(main())
