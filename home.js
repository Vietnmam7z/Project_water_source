document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("wateringBtn");

    btn.addEventListener("click", () => {
        fetch("/toggle")
            .then(response => response.text())
            .then(data => console.log("ESP32:", data))
            .catch(err => console.error("Lỗi gửi yêu cầu:", err));
    });
});

function updateSensorData() {
    fetch('/sensor')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperatureValue').textContent = data.temperature;
            document.getElementById('humidityValue').textContent = data.humidity;
        })
        .catch(error => {
            console.error('Lỗi khi lấy dữ liệu cảm biến:', error);
        });
}

function updateButtonState() {
    fetch('/status')
        .then(res => res.json())
        .then(data => {
            const btn = document.getElementById("wateringBtn");
            const isActive = data.relay_state;

            if (isActive) {
                btn.classList.add("active");
                btn.textContent = "Ngưng tưới";
            } else {
                btn.classList.remove("active");
                btn.textContent = "Tưới nước";
            }
        })
        .catch(err => console.error("Lỗi lấy trạng thái relay:", err));
}

setInterval(updateButtonState, 200);

setInterval(updateSensorData, 5000);

updateSensorData();
