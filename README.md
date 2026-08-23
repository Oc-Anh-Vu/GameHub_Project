# 🎮 Python Game Hub

Một dự án cá nhân xây dựng tổ hợp các trò chơi cổ điển trên Desktop sử dụng ngôn ngữ Python và thư viện giao diện Tkinter. 

Dự án này được thiết kế theo nguyên tắc Module hóa (OOP), trong đó mỗi trò chơi hoạt động độc lập và được quản lý bởi một Menu điều hướng trung tâm (Taskbar).

---

## 🎯 Tính năng nổi bật

* **Giao diện Menu Điều hướng (Taskbar):** Dễ dàng chuyển đổi qua lại giữa các tựa game mà không cần mở nhiều cửa sổ.
* **Cấu trúc Module hóa:** Mỗi game được lưu trữ trong một tệp `.py` riêng biệt, giúp mã nguồn gọn gàng, dễ bảo trì và dễ mở rộng.
* **Tích hợp sẵn Cờ Caro (Gomoku):** 
  * Bàn cờ 10x10.
  * Thuật toán kiểm tra thắng/thua chính xác (5 quân liên tiếp).
  * Giao diện trực quan, đổi màu theo lượt người chơi.
* **Khả năng mở rộng:** Dễ dàng bổ sung các trò chơi mới (Sudoku, Minesweeper, Othello...) chỉ bằng cách thêm file mới và khai báo trong file Main.

---

## 📂 Cấu trúc dự án

\`\`\`text
GameHub_Project/
│
├── main.py        # Ứng dụng trung tâm, quản lý Menu và điều hướng
├── caro.py        # Logic và giao diện của game Cờ Caro (Gomoku)
├── sudoku.py      # Bộ khung cho game Sudoku (Đang phát triển)
└── README.md      # Tài liệu giới thiệu dự án
\`\`\`

---

## 🚀 Hướng dẫn cài đặt và sử dụng

### 1. Yêu cầu hệ thống
* Đã cài đặt **Python 3.x** (Khuyến nghị bản mới nhất).
* Thư viện `Tkinter` (Thường được tích hợp sẵn khi cài đặt Python).

### 2. Cách chạy ứng dụng
1. Mở Terminal / Command Prompt và di chuyển đến thư mục dự án.
2. Chạy tệp tin chính bằng lệnh sau:
   \`\`\`bash
   python main.py
   \`\`\`
3. Ứng dụng sẽ mở ra với trò chơi mặc định là Cờ Caro.
4. Sử dụng thanh Menu ở góc trên cùng để chuyển đổi sang các trò chơi khác.

---

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python 
* **Giao diện người dùng (GUI):** Tkinter (Thư viện chuẩn của Python)
* **IDE Khuyến nghị:** Visual Studio Code (VS Code)

---
*Dự án được phát triển nhằm mục đích rèn luyện tư duy lập trình và thiết kế giao diện với Python.*