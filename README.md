# **DỰ ÁN MẠCH NƯỚC TỰ ĐỘNG (WATER SOURCE PROJECT)**

Đây là dự án cá nhân nhằm mục đích tìm hiểu về IoT và các ứng dụng thực tiễn trong đời sống. Dự án sử dụng van điện từ làm thành phần chấp hành chính, được điều khiển bởi vi điều khiển ESP32. Ngoài ra, hệ thống còn tích hợp một website nội bộ (LAN) để người dùng có thể dễ dàng điều khiển từ xa.

---

## **Mục lục**
**[I. Linh kiện cần thiết](#i-linh-kiện-cần-thiết)** | **[II. Sơ đồ và cấu trúc](#ii-sơ-đồ-và-cấu-trúc)** | **[III. Hướng dẫn cài đặt & sử dụng](#iii-hướng-dẫn-cài-đặt--sử-dụng)** | **[IV. Tổng kết dự án](#iv-tổng-kết-dự-án)**
---

## **I. Linh kiện cần thiết**

### **1. ESP32 (1 mạch)**
<img src="https://github.com/user-attachments/assets/958f224b-31e8-422d-88a7-6d5eaf772c0c" width="400" />

* Là vi điều khiển phổ biến với giá thành rẻ, hỗ trợ nhiều cổng kết nối.
* Tích hợp sẵn Wi-Fi và Bluetooth, phù hợp cho các dự án kết nối không dây, tạo web server, hoặc gửi dữ liệu lên cơ sở dữ liệu.

### **2. Van điện từ (1 cái)**
<img src="https://github.com/user-attachments/assets/fb3fa30f-dd41-431e-b144-6199e3ee31cc" width="400" />

* Đây là thiết bị chính, có nhiệm vụ đóng/mở nguồn nước. Van hoạt động dựa trên nguyên lý từ trường: khi được cấp điện, nam châm điện sẽ mở van và van sẽ tự động đóng lại khi ngắt điện, giúp tránh lãng phí nước nếu có sự cố về điện.
* Thị trường có nhiều loại van đa dạng về kích thước ống, tính năng (mở thủ công, điều chỉnh lưu lượng), và giá thành.
* <span style="color:red">**Lưu ý:** Dự án này sử dụng van điện một chiều (DC). Khi mua, cần chọn đúng loại van (DC) và đúng hiệu điện thế để lựa chọn adapter nguồn tương thích.</span>

### **3. Module Relay (1 mạch)**
<img src="https://github.com/user-attachments/assets/84ff37b7-8ea2-4191-949d-e66b278cbac7" width="400" />

* Do ESP32 không thể trực tiếp điều khiển các thiết bị có điện áp cao như van điện từ, module relay được sử dụng làm cầu nối.
* Module này nhận tín hiệu điều khiển từ ESP32 để kích hoạt công tắc (khóa K), cho phép dòng điện từ adapter cấp cho van điện từ.
* <span style="color:red">**Lưu ý:** Cần chọn module relay có điện áp kích hoạt tương thích với mức logic của ESP32 (thường là 3.3V hoặc 5V) và phù hợp với adapter cấp nguồn cho nó.</span>

### **4. Cảm biến nhiệt độ - độ ẩm (1 cái) (Tùy chọn)**
<img src="https://github.com/user-attachments/assets/88fa0cbc-9f71-4935-a0bd-8552d7eb014e" width="400" />

* Là cảm biến phổ biến trong các lĩnh vực nông nghiệp, nhà thông minh, khí tượng,... với ưu điểm giá rẻ, dễ lập trình và sử dụng.
* Trong phạm vi dự án này, cảm biến chưa được khai thác nhiều nhưng là một hướng phát triển tiềm năng (xem mục IV).

### **5. Nút nhấn (1 cái)**
<img src="https://github.com/user-attachments/assets/30d51312-c092-4492-8739-1e28841de021" width="400" />

* Là thiết bị đầu vào đơn giản và đa dụng. Trong dự án này, nút nhấn đóng vai trò là một phương thức điều khiển dự phòng.
* Có thể phát triển thêm các chức năng như nhấn giữ, nhấn đúp để thực hiện các tác vụ khác nhau.
* <span style="color:red">**Lưu ý:** Cần tối thiểu 1 nút nhấn. Đây là cơ chế an toàn, cho phép người dùng bật/tắt van thủ công trong trường hợp mạng Wi-Fi yếu hoặc web server không thể truy cập.</span>

### **6. Adapter nguồn (2 cái)**
<img src="https://github.com/user-attachments/assets/f65c5eb6-4cac-46bc-826a-004de2d1c698" width="400" />

* Cung cấp nguồn điện cho các thành phần của mạch.
* Dự án cần 2 adapter vì van điện từ thường yêu cầu điện áp cao (12V trở lênlên), trong khi ESP32, relay và cảm biến chỉ cần điện áp thấp (3.3V - 5V).
* *Giải pháp thay thế:* Có thể sử dụng một adapter duy nhất kết hợp với mạch hạ áp. Do dự án này nhằm tối ưu thời gian và chi phí nen sẽ sử dụng 2 adapter

### **7. Jack nối DC (2 cái)**
<img src="https://github.com/user-attachments/assets/0ed00a79-4364-4ead-9e53-75260f69248b" width="400" />

* Dùng để kết nối adapter với mạch điện một cách dễ dàng. Số lượng tùy thuộc vào số adapter sử dụng.

### **8. Linh kiện khác**
* Breadboard (1 cái)
* Dây cắm breadboard (đực - cái)
* Cáp Micro-USB (loại hỗ trợ truyền dữ liệu)
* Dây điện, băng keo cách điện, tua vít.

### **9. Thiết bị hỗ trợ (Tùy chọn)**
* Đồng hồ vạn năng.

<span style="color:red">**P/S:** Cấu hình tham khảo cho dự án này (ưu tiên chi phí thấp): Van điện từ 24VDC (ống 13mm), Module relay 5V, Cảm biến DHT11. Nếu bạn sử dụng linh kiện khác (đặc biệt là cảm biến), cần phải điều chỉnh lại code cho phù hợp.</span>

---

## **II. Sơ đồ và cấu trúc**

### **1. Sơ đồ tổng thể**
<img src="https://github.com/user-attachments/assets/ef3af815-6a3f-4062-b02d-f25d4845e416" width="400" />

### **2. Sơ đồ nối dây chi tiết**
<img src="https://github.com/user-attachments/assets/8514e6b9-6c69-4f0e-8c53-507caed5c96d" width="400" />

* **Kết nối van điện từ và Relay:**
    * Van điện từ thường có 2 dây không phân cực. Một dây nối vào cổng **NO** (Normally Open) của relay.
    * Dây còn lại của van nối vào cực **âm (-)** của adapter 24V.
    * Cổng **COM** của relay nối vào cực **dương (+)** của adapter 24V.
* **Kết nối tín hiệu với ESP32:**
    * Chân tín hiệu (DATA) của **nút nhấn** nối vào cổng **GPIO 27**.
    * Chân tín hiệu (DATA) của **cảm biến DHT11** nối vào cổng **GPIO 26**.
    * Chân tín hiệu (IN) của **module relay** nối vào cổng **GPIO 32**.
* <span style="color:red">**Lưu ý:** Tên chân tín hiệu có thể khác nhau tùy loại linh kiện (ví dụ: IN, OUT, S,...). Luôn tham khảo datasheet của linh kiện nếu không chắc chắn.</span>

---

## **III. Hướng dẫn cài đặt & sử dụng**

### **1. Phần mềm**
Dự án sử dụng ngôn ngữ **MicroPython** và được lập trình bằng phần mềm **Thonny IDE** vì tính trực quan và tốc độ phát triển nhanh.
* **Link tải Thonny:** [https://thonny.org](https://thonny.org)
* <span style="color:red">**Lưu ý:** Không phải vi điều khiển nào cũng hỗ trợ MicroPython. Mặc định, ESP32 chưa có sẵn firmware MicroPython, bạn cần phải nạp firmware trước khi sử dụng. Có rất nhiều hướng dẫn chi tiết trên Internet về cách thực hiện việc này.</span>

### **2. Các bước chạy chương trình**
1.  **Kết nối linh kiện:** Lắp ráp mạch theo sơ đồ ở mục II.
2.  **Kết nối ESP32:** Mở Thonny và kết nối với ESP32 thông qua cáp Micro-USB.
3.  **Tải code lên thiết bị:** Chuyển toàn bộ các file trong thư mục dự án vào bộ nhớ của ESP32.
4.  **Cấu hình Wi-Fi:** Mở file `config.py` và chỉnh sửa lại tên Wi-Fi (`ssid`) và mật khẩu (`password`) của mạng bạn muốn kết nối.
5.  **Chạy chương trình:** Mở file `main.py` và nhấn phím **F5** (hoặc nút Run) để thực thi.
6.  **Truy cập website:** Theo dõi output trên màn hình Console của Thonny. Nếu kết nối thành công, bạn sẽ thấy dòng thông báo:
    `✅ Đã kết nối Wi-Fi. IP: x.x.x.x`
    Sử dụng địa chỉ IP (`x.x.x.x`) này trên trình duyệt của một thiết bị (máy tính, điện thoại) đang kết nối cùng mạng Wi-Fi để truy cập vào trang điều khiển.

<span style="color:red">**Lưu ý:**</span>
* <span style="color:red">Nếu không thấy dòng thông báo "✅ Đã kết nối Wi-Fi...", hãy kiểm tra lại tên và mật khẩu Wi-Fi trong file `config.py`.</span>
* <span style="color:red">Đây là web server nội bộ (LAN), chỉ có thể truy cập từ các thiết bị trong cùng một mạng.</span>
* <span style="color:red">Địa chỉ IP của ESP32 có thể thay đổi mỗi khi kết nối lại với một mạng Wi-Fi khác.</span>

---

## **IV. Tổng kết dự án**

### **1. Ưu điểm**
* Dự án đơn giản, dễ tiếp cận cho người mới bắt đầu.
* Khai thác mô hình đa luồng (RTOS) giúp xử lý đồng thời nhiều tác vụ (đọc cảm biến, nhận tín hiệu nút nhấn, quản lý server).
* Là nền tảng tốt để tìm hiểu về kết nối phần cứng, lập trình nhúng và phát triển web server cơ bản.
* Có tính ứng dụng thực tế cao.

### **2. Nhược điểm**
* Chi phí cho toàn bộ linh kiện có thể tương đối cao nếu mua mới hoàn toàn.
* Phạm vi dự án còn đơn giản, chưa khai thác hết tiềm năng của các thiết bị.

### **3. Hướng phát triển**
* **Hệ thống tưới tiêu tự động:**
    * Kết hợp thêm cảm biến độ ẩm đất để tự động tưới khi đất khô.
    * Phát triển giao diện web cho phép người dùng lập lịch tưới (theo giờ, theo ngày).
* **Hệ thống phun sương làm mát:**
    * Sử dụng cảm biến nhiệt độ - độ ẩm để tự động kích hoạt hệ thống phun sương khi nhiệt độ môi trường vượt ngưỡng cài đặt.
* **Vòi rửa tay tự động:**
    * Tích hợp cảm biến hồng ngoại (IR) hoặc cảm biến siêu âm để phát hiện chuyển động, tự động mở/đóng vòi nước.
* **Hệ thống thông minh hơn:**
    * Kết hợp dữ liệu thời tiết từ Internet để quyết định có nên tưới cây hay không (ví dụ: nếu trời sắp mưa thì không cần tưới).
