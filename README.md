PROJECT WATER SOURCE
Đây là dự án cá nhân nhằm tìm hiểu IoT và có thể ứng dụng vào đời sống.
Dự án này sử dụng van điện từ làm thành phần chính để hoạt động. Bênh cạnh đó còn có sử dụng thêm esp32 để điều khiển quá trình đóng mở của van điện từ này. Ngoài ra, hệ thống còn có sử dụng thêm một website LAN để dễ dàng điều khiển từ xa hơn.
I. Các thành phần linh kiện 
1. esp32 ( 1 mạch)
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/958f224b-31e8-422d-88a7-6d5eaf772c0c" />
Đây là một thiết bị vi điều khiển phổ biến với các ưu điểm như giá thành rẻ, có nhiều port kết nối nên hỗ trợ nhiều dự án, có hỗ trợ cả wifi và bluetooth cho các dự án kết nối không dây, tạo mini web, hay gửi dữ liệu lên cơ sở dữ liệu.
2. Van điện từ
<img width="961" height="1280" alt="image" src="https://github.com/user-attachments/assets/fb3fa30f-dd41-431e-b144-6199e3ee31cc" />
Đây là thiết bị chính cho ra nguồn nước. Với ưu điểm ngoài dẫn nước đa phần chúng có thể dẫn được khí, dầu,..., mà vẫn đảm bảo an toàn. Thiết bị khi được dẫn điện sẽ mở van bằng nam châm và sẽ tự đóng van khi không có điện, điều đó đảm bảo nếu trục trặc về nguồn điện thì vẫn đảm bảo không hao phí nước.
Có khá nhiều dòng van trên thị trường đa dạng về kích thước ống, tính năng mở van thủ công, điều chỉnh được độ mở van để tăng độ lớn nhỏ của sức nước; tương ứng với các tính năng đó giá thành của thiết bị có thể tăng hoặc giảm.
Lưu ý: Đối với dư án này van nước sẽ dùng điện một chiều nên khi lựa chọn van hãy xem thông tin có hỗ trợ dòng DC hay không? Đồng thời cũng chọn lựa đúng hiệu điện thế để chọn mua adapter đúng.
3. Module relay ( 1 mạch)
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/84ff37b7-8ea2-4191-949d-e66b278cbac7" />
Để có thể ứng dụng được mạch esp32 vào van điện từ thì dự án yêu cầu dùng thêm một module relay. Bởi vì hầu như các van điện từ không có khả năng lập trình, cũng như có thiết bị hỗ trợ lặp trình đi kèm.
Module relay là một module lập trình phục vụ mục đích biến các thiết bị gia dụng có khả năng vào mạng Internet ( chủ yếu nằm ở khả năng bật tắt). Module này sẽ dùng tín hiệu từ vi điều khiển để khích hoạt khóa K của relay và từ đó cho phép dòng điện dẫn vào thiết bị dựa vào mong muốn của người dùng.
Lưu ý: Chọn đúng adapter để kích module relay vì có nhiều loại relay có hiệu điện thế kích hoạt khác nhau.
4. Cảm biến nhiệt độ - độ ẩm (1 cái) ( không bắt buộc)
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/88fa0cbc-9f71-4935-a0bd-8552d7eb014e" />
Cảm biến nhiệt độ - độ ẩm là loại cảm biến thường dùng trong các lĩnh vực như nông nghiệp, nhà thông minh, khí tượng,....  Một trong những đặc điểm đáng chú ý của nó là có khá nhiều loại mẫu mã, giá thành rẻ, dễ thao tác, dễ lập trình.
Đối với dự án này vẫn chưa dùng quá nhiều với thiết bị này nhưng có thể mở rộng thêm ( xem phần III.).
5. Nút nhấn(1 cái)
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/30d51312-c092-4492-8739-1e28841de021" />
Nút nhấn cũng là một trong các thiết bị đa dụng và rất dễ lập trình.
Đối với dự án này hoàn toàn có thể phát triển thêm với khả năng của nút nhấn bằng cách thêm chức năng như nhấn giữ, nhấn liên tục. Cũng hoàn toàn có thể trang bị thêm nút nhấn để thêm tính năng nếu muốn.
Chú ý: Tối thiểu phải có 1 nút nhấn. Đây là hệ thống đảm bảo khi điều kiện hạ tầng về mạng quá yếu, dùng cho mục đích nếu web không lên được để bật tắt thiết bị khi cần dùng mà không cần thông qua web.
6. Adapter ( 2 cái)
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/f65c5eb6-4cac-46bc-826a-004de2d1c698" />
Mục đích chính của thiết bị adapter này là để cung cấp điện cho esp32,module relay, cảm biến nhiệt độ - độ ẩm, van điện từ.
Nguyên do sử dụng 2 adapter là vì mạch có van điện từ thường dùng điện từ 12V trở lên nhưng phần lớn các thiết bị còn lại đều có thể dùng chỉ từ 3.3 - 5V. Tuy nhiên, hoàn toàn có thể trang bị thêm mạch hạ áp hoặc biến áp để giảm thành 1 adapter.
Do đối với dự án nhỏ này để đảm bảo chi phí cũng như thời gian nên sẽ chọn 2 adapter.
7. Đầu đổi adapter sang nối dây kim ( 2 cái).
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/0ed00a79-4364-4ead-9e53-75260f69248b" />
Số lượng có thể tùy vào số adapter dự án có.
8. Các thiết bị khác - breadboard ( 1 cái), dây nối ( loại đực - cái), dây micro - usb ( tìm loại có thể truyền dữ liệu), dây điện (2 dây), băng keo điện, vít.
9. Thiết bị hỗ trợ - Đồng hồ đo ( không bắt buộc).
P/S: Đối với dự án này các thiết bị được chọn như van điện từ ( 24VDC - ống 13mm), module relay (5V kích), cảm biến nhiệt độ - độ ẩm ( DHT11). Mục đích chính là để tiết kiệm chi phí nên hoàn toàn có thể lựa chọn các thiết bị khác có thông số khác. Lưu ý là nếu sử dụng cảm biến nhiệt độ - độ ẩm khác thì trong code sẽ cần chỉnh sửa khác
Trong file:
config.py 
<img width="453" height="39" alt="image" src="https://github.com/user-attachments/assets/3462b4ed-2a7d-4e67-b1f7-bc3b73f3482c" />
Có thể đổi lại file dht11.py do hàm không chạy được. Khi lắp mạch nên lắp từng thiết bị và chạy thử các hàm test ( có thể gerate các code này từ AI) để xem thiết bị có hoạt động đúng không, đồng thời có thể chỉnh sửa trong file thư viện đa phàn là DHT11 nếu chọn cảm biến khác hoặc chân thiết lặp trong config nếu chọn chân khác.
II. Cấu trúc dự án
1. Sơ đồ tổng thể
<img width="461" height="462" alt="So do tong the drawio" src="https://github.com/user-attachments/assets/ef3af815-6a3f-4062-b02d-f25d4845e416" />
2. Sơ đồ nối dây
<img width="591" height="632" alt="So do noi day drawio" src="https://github.com/user-attachments/assets/8514e6b9-6c69-4f0e-8c53-507caed5c96d" />
Lưu ý: Các dây Data trong hình là dây tín hiệu của các thiết bị ( tùy từng thiết bị sẽ có tên khác nhau như, in, out,...)
Do các adapter sẽ nối với đầu chuyển đổi nên giờ sẽ gọi đầu chuyển đổi của adapter là cực âm và dương
Phần van điện từ có 2 dây, do chúng thường hỗ trợ cả điện 2 chiều và 1 chiều nên không quan trong phần nối, tốt nhất vẫn nên đọc hướng dẫn nối nếu có. Ở đây ta sẽ chọn 1 dây của van điện từ để nối vào cổng NO của module relay tượng trưng cho đầu dương, còn đầu còn lại sẽ nối trực tiếp với cực âm của adapter 24V
Đối với cực dương của adapter 24V sẽ nối với cổng COM của module relay
Các cổng (port) của esp32 nối với data của các thiết bị theo code: data nút bấm nối vào port 27, data DHT11 nối vào port 26, data của module relay nối vào port 32.
III. Code
1. Phần mềm lặp trình
Dự án được lặp trình bằng phần mềm Thonny thông qua sử dụng ngôn ngữ microPython cho sự trực quan và thời gian thiết kế. Link tải: https://thonny.org/
Lưu ý: Các thiết bị vi điều khiển không đảm bảo là hoạt động được trên microPython. Ngoài ra, mặc định các thiết bị này sẽ không có firmware để chạy microPython dù có hỗ trợ hay không. Tuy nhiên, hoàn toàn có thể tìm các video hướng dẫn tải và boot trên Internet.
3. Hướng dẫn chạy chương trình.
Nếu dự án đảm bảo đúng các thiết bị cho mạch như đã giới thiệu trong phần I thì hoàn toàn có thể dùng code này.
Bước 1: Kết nối các linh kiện.
<img width="1280" height="961" alt="image" src="https://github.com/user-attachments/assets/82f8b62e-4388-421c-9f9f-4ff672e41a1e" />
Bước 2: Mở phần mềm Thonny lên và kết nối vào esp32
<img width="554" height="60" alt="image" src="https://github.com/user-attachments/assets/ebed99bd-3f7d-45ba-aeef-bf6547534959" />
Bước 3: Save toàn bộ các file có trong thư mục vào thiết bị
<img width="189" height="328" alt="image" src="https://github.com/user-attachments/assets/e28bb055-7efc-4096-8c6f-f59594fde8d5" />
Bước 4: Mở file config và chỉnh lại tên wifi và mật khẩu
<img width="213" height="97" alt="image" src="https://github.com/user-attachments/assets/dbc1ef13-097d-4856-a3e5-a1dfb360a5f4" />
Bước 5: Mở file main.py và chạy bằng nút F5 hoặc <img width="31" height="32" alt="image" src="https://github.com/user-attachments/assets/71de4ab5-415c-4305-ae1f-2a332f8f3c69" />
Bước 6: Nếu muốn bật web thì hãy chú ý đến phần in ra trên console; nếu thành công thì sẽ có ký tự "✅ Đã kết nối Wi-Fi. IP: x.x.x.x". Phần "x.x.x.x" này sẽ là ip đẻe truy cập có thể dùng nó để paste vào trình duyệt để truy cập.
Lưu ý:
Nếu không có dòng "✅ Đã kết nối Wi-Fi ..." sau khi hiện chữ "Server start" có nghĩa là chưa kết nối với wifi. Có thể là do nhập chưa đúng tên wifi hay mật khẩu.
Đây là web LAN nên phải dùng thiết bị đã kết nối đúng mạng của esp32 dùng để tạo web thì mới vào được.
Ngoài ra dù thiết bị chạy ở wifi với ip x thì sang wifi khác nó hoàn toàn có thể đổi thành wifi y,z,...
IV. Đặc điểm của dự án
1. Ưu điểm
Là dự án đơn giản, dễ thực hiện.
Khai thác mô hình RTOS để chạy thiết bị.
Có nhiều mô hình để tìm hiểu như RTOS, nhấn thả nút với RTOS, tạo website, kết nối phần cứng.
Hoàn toàn ứng dụng được trong thực tế.
2. Nhược điểm
Tuy nói là dự án nhỏ nhưng chi phí để chi trả cho các thiết bị không thật sự nhỏ ( nếu mua toàn bộ)
Đây là dự án cá nhân và cũng không có mục đích quá rõ rang nên nó chưa thực sự hoàn chỉnh. Vì bản chất dự án này chỉ có van nước thôi.
3.Triển vọng phát triển
Có thể nói điểm yếu chính của dự án này là chưa hoàn thiện nhưng nó cũng tạo nên rất hiều hướng phát triển.
Phát triển theo hướng tưới tiêu tự động: Ta hoàn toàn có thể nối thêm ống nước và các vòi phun thành một sơ đồ vườn tưới. Ngoài ra, còn có thể thêm các chức năng như tự động tưới, có thể cập nhật thêm nút bấm vào hay tạo lập lịch tưới
Phát triển theo hướng vời phun nước tạo ẩm: Ở hướng này khá giống tưới nước tự động ở sơ đồ ống nước và vòi phun. Ta có thể tận dụng thêm cảm biến nhiệt độ - độ ẩm để đo nhiệt độ môi trường từ đó để hệ thống tự động phun nước làm mát không khí.
Phát triển theo hướng vòi rửa tay tự động: Có thể trang bị thêm cảm biến hồng ngoại để đọc vật cản. Từ đó tạo thành vòi nước khi tay đặt gần vật cảm biến.
Có thể ứng dụng thêm cảm biến nhiệt độ - độ ẩm để biết trời đang nắng hay mưa để mở van.







