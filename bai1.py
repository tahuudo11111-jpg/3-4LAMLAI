import tkinter as tk
from tkinter import messagebox
import math

def tinh_the_tich():
    try:
        # Lấy giá trị diện tích từ ô nhập
        S = float(entry_s.get())
        
        # Tính bán kính từ diện tích mặt cầu: S = 4πR²
        R = math.sqrt(S / (4 * math.pi))
        
        # Tính thể tích: V = 4/3 πR³
        V = (4/3) * math.pi * (R**3)
        
        # Hiển thị kết quả
        label_kq.config(text=f"Thể tích V = {V:.6f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính thể tích hình cầu")

# Nhãn và ô nhập diện tích
label_s = tk.Label(root, text="Nhập diện tích S của mặt cầu:")
label_s.pack(pady=5)

entry_s = tk.Entry(root, width=20)
entry_s.pack(pady=5)

# Nút tính toán
btn_tinh = tk.Button(root, text="Tính thể tích", command=tinh_the_tich)
btn_tinh.pack(pady=10)

# Nhãn kết quả
label_kq = tk.Label(root, text="Thể tích V sẽ hiển thị ở đây")
label_kq.pack(pady=10)

# Chạy vòng lặp giao diện
root.mainloop()
