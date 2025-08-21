# wifi_connect.py
import esp
import network
import time
import ubinascii

import network
import ubinascii
import utime

def start_wifi(wlan_id, wlan_pass, timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    mac = ubinascii.hexlify(wlan.config('mac'), ':').decode()
    print("MAC:", mac)

    if not wlan.isconnected():
        print("Đang kết nối Wi-Fi...")
        wlan.connect(wlan_id, wlan_pass)

        start_time = utime.time()
        while not wlan.isconnected():
            if utime.time() - start_time > timeout:
                print("⛔ Kết nối Wi-Fi thất bại sau", timeout, "giây")
                return None
            utime.sleep(1)

    ip = wlan.ifconfig()[0]
    print("✅ Đã kết nối Wi-Fi. IP:", ip)
    return ip

def get_rssi():
    """Trả về RSSI hiện tại của kết nối Wi-Fi"""
    sta = network.WLAN(network.STA_IF)
    if sta.isconnected():
        return sta.status('rssi')  # Ví dụ: -45 dBm
    return -100  # Mặc định khi chưa kết nối

def rssi_to_bars(rssi):
    """Chuyển RSSI thành số vạch sóng (0–4)"""
    if rssi >= -50:
        return 4
    elif rssi >= -60:
        return 3
    elif rssi >= -70:
        return 2
    elif rssi >= -80:
        return 1
    else:
        return 0