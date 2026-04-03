import tkinter as tk
from tkinter import messagebox
import math

def calculate_nested_sqrt():
    try:
        # Lấy giá trị n từ ô nhập liệu
        n_str = entry_n.get()
        if not n_str:
            messagebox.showwarning("Thông báo", "Vui lòng nhập số n!")
            return
            
        n = int(n_str)
        if n < 1:
            messagebox.showwarning("Lỗi", "n phải là số nguyên dương (n >= 1)!")
            return

        # Tính toán theo công thức lồng từ trong ra ngoài
        # S = sqrt(1)
        # S = cuberoot(2 + S) ...
        # Công thức tổng quát tại bước i: S = (i + S)^(1/(i+1))
        
        s = math.sqrt(1) # Đây là bước căn bậc 2 của 1
        
        for i in range(2, n + 1):
            s = math.pow(i + s, 1 / (i + 1))
            
        # Hiển thị kết quả làm tròn 5 chữ số thập phân như ví dụ
        result_label.config(text=f"Kết quả: {s:.5f}", fg="#2E7D32")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ!")

# Thiết lập giao diện đồ họa
root = tk.Tk()
root.title("Tính Căn Số Liên Tục")
root.geometry("400x250")
root.resizable(False, False)

# Tiêu đề bài tập
header = tk.Label(root, text="Bài 49: Tính căn số liên tục", font=("Arial", 12, "bold"))
header.pack(pady=10)

# Khung nhập liệu
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nhập n:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
entry_n = tk.Entry(frame_input, font=("Arial", 11), width=10, justify='center')
entry_n.grid(row=0, column=1, padx=5)
entry_n.focus_set()

# Nút tính toán
btn_calc = tk.Button(root, text="Tính Kết Quả", command=calculate_nested_sqrt, 
                     bg="#1976D2", fg="white", font=("Arial", 10, "bold"), 
                     padx=20, pady=5)
btn_calc.pack(pady=15)

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="Kết quả: ---", font=("Consolas", 14, "bold"))
result_label.pack(pady=10)

# Chạy ứng dụng
root.mainloop()
