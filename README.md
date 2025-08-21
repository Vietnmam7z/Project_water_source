# PROJECT WATER SOURCE

Dự án cá nhân nhằm tìm hiểu về IoT và ứng dụng vào đời sống.  
Sử dụng van điện từ làm thành phần chính, ESP32 để điều khiển, và website LAN để điều khiển từ xa.

---

## **I. Các thành phần linh kiện**

### 1. ESP32 (1 mạch)  
<img src="https://github.com/user-attachments/assets/958f224b-31e8-422d-88a7-6d5eaf772c0c" width="400" />

Vi điều khiển phổ biến, giá rẻ, hỗ trợ Wi-Fi và Bluetooth, dùng để tạo web mini hoặc gửi dữ liệu.

### 2. Van điện từ  
<img src="https://github.com/user-attachments/assets/fb3fa30f-dd41-431e-b144-6199e3ee31cc" width="400" />

Thiết bị chính để dẫn nước, khí, dầu,... Khi có điện, van mở bằng nam châm; khi mất điện, van tự đóng.

<span style="color:red">**Lưu ý:** Van dùng điện một chiều. Kiểm tra thông số hỗ trợ dòng DC và chọn đúng hiệu điện thế để mua adapter phù hợp.</span>

### 3. Module Relay (1 mạch)  
<img src="https://github.com/user-attachments/assets/84ff37b7-8ea2-4191-949d-e66b278cbac7" width="400" />

Giúp ESP32 điều khiển van điện từ. Relay nhận tín hiệu từ vi điều khiển để bật/tắt thiết bị.

<span style="color:red">**Lưu ý:** Chọn đúng adapter vì mỗi loại relay có hiệu điện thế kích hoạt khác nhau.</span>

### 4. Cảm biến nhiệt độ - độ ẩm (1 cái, không bắt buộc)  
<img src="https://github.com/user-attachments/assets/88fa0cbc-9f71-4935-a0bd-8552d7eb014e" width="400" />

Thường dùng trong nông nghiệp, nhà thông minh,... Có nhiều mẫu mã, dễ lập trình.

### 5. Nút nhấn (1 cái)  
<img src="https://github.com/user-attachments/assets/30d51312-c092-4492-8739-1e28841de021" width="400" />

Thiết bị đa dụng, dễ lập trình. Có thể thêm chức năng như nhấn giữ, nhấn liên tục.

<span style="color:red">**Chú ý:** Tối thiểu phải có 1 nút nhấn để đảm bảo hệ thống hoạt động khi mạng yếu hoặc không thể truy cập web.</span>

### 6. Adapter (2 cái)  
<img src="https://github.com/user-attachments/assets/f65c5eb6-4cac-46bc-826a-004de2d1c698" width="400" />

Cung cấp điện cho ESP32, relay, cảm biến, van điện từ. Dùng 2 adapter vì van cần 12V trở lên, còn các thiết bị khác chỉ cần 3.3V–5V.

### 7. Đầu đổi adapter sang dây kim (2 cái)  
<img src="https://github.com/user-attachments/assets/0ed00a79-4364-4ead-9e53-75260f69248b" width="400" />

Số lượng tùy thuộc vào số adapter.

### 8. Các thiết bị khác  
Breadboard, dây nối (đực–cái), dây micro-USB (truyền dữ liệu), dây điện, băng keo điện, vít.

### 9. Thiết bị hỗ trợ  
Đồng hồ đo (không bắt buộc).

<span style="color:red">**P/S:** Dự án sử dụng van điện từ 24VDC (ống 13mm), relay 5V, cảm biến DHT11. Nếu dùng cảm biến khác, cần chỉnh sửa code.</span>

---

## **II. Cấu trúc dự án**

### 1. Sơ đồ tổng thể  
<img src="https://github.com/user-attachments/assets/ef3af815-6a3f-4062-b02d-f25d4845e416" width="400" />

### 2. Sơ đồ nối dây  
<img src="https://github.com/user-attachments/assets/8514e6b9-6c69-4f0e-8c53-507caed5c96d" width="400" />

<span style="color:red">**Lưu ý:** Các dây Data là dây tín hiệu. Van điện từ có thể nối không phân cực, nhưng nên đọc hướng dẫn. Các cổng ESP32: nút nhấn → port 27, DHT11 → port 26, relay → port 32.</span>

---

## **III. Code**

### 1. Phần mềm lập trình  
Sử dụng Thonny với ngôn ngữ MicroPython.  
Link tải: [https://thonny.org](https://thonny.org)

<span style="color:red">**Lưu ý:** ESP32 cần nạp firmware MicroPython. Có thể tìm video hướng dẫn trên Internet.</span>

### 2. Hướng dẫn chạy chương trình

- **Bước 1:** Kết nối các linh kiện  
- **Bước 2:** Mở Thonny và kết nối ESP32  
- **Bước 3:** Lưu toàn bộ file vào thiết bị  
- **Bước 4:** Mở file `config.py` và chỉnh tên Wi-Fi, mật khẩu  
- **Bước 5:** Mở file `main.py` và chạy bằng F5  
- **Bước 6:** Kiểm tra console. Nếu hiện "✅ Đã kết nối Wi-Fi. IP: x.x.x.x" thì dùng IP đó để truy cập web LAN

<span style="color:red">**Lưu ý:** Nếu không thấy dòng kết nối Wi-Fi, kiểm tra lại tên và mật khẩu. Web LAN chỉ truy cập được khi thiết bị cùng mạng với ESP32.</span>

---

## **IV. Đặc điểm của dự án**

### 1. Ưu điểm  
- Dễ thực hiện  
- Khai thác mô hình RTOS  
- Tìm hiểu nhiều mô hình: RTOS, website, phần cứng  
- Có thể ứng dụng thực tế

### 2. Nhược điểm  
- Chi phí thiết bị không nhỏ nếu mua toàn bộ  
- Dự án cá nhân, chưa hoàn chỉnh

### 3. Triển vọng phát triển  
- **Tưới tiêu tự động:** Thêm vòi phun, lịch tưới  
- **Tạo ẩm:** Dùng cảm biến để phun nước làm mát  
- **Vòi rửa tay tự động:** Thêm cảm biến hồng ngoại  
- **Dự báo thời tiết:** Dùng cảm biến để mở van khi trời nắng
