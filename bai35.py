import tkinter as tk
from tkinter import messagebox
import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm xử lý khi nhấn nút "Kiểm tra"
def solve():
    try:
        n = int(entry_n.get())
        if n <= 0:
            messagebox.showwarning("Lỗi", "Vui lòng nhập số nguyên dương!")
            return
        
        if is_prime(n):
            result_label.config(text=f"{n} là số nguyên tố.", fg="green")
            sub_result_label.config(text="")
        else:
            result_label.config(text=f"{n} không là số nguyên tố.", fg="red")
            
            # Tìm số nguyên tố gần nhất và bé hơn n
            found = False
            for i in range(n - 1, 1, -1):
                if is_prime(i):
                    sub_result_label.config(text=f"Số nguyên tố bé hơn gần nhất: {i}", fg="blue")
                    found = True
                    break
            
            if not found:
                sub_result_label.config(text="Không có số nguyên tố nào bé hơn n.", fg="orange")
                
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ!")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Kiểm tra Số Nguyên Tố")
root.geometry("400x250")
root.eval('tk::PlaceWindow . center') # Căn giữa màn hình

# Giao diện
label_instruction = tk.Label(root, text="Nhập số nguyên dương n:", font=("Arial", 11))
label_instruction.pack(pady=10)

entry_n = tk.Entry(root, font=("Arial", 12), justify='center')
entry_n.pack(pady=5)
entry_n.focus_set()

btn_check = tk.Button(root, text="Kiểm tra", command=solve, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=15)
btn_check.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack()

sub_result_label = tk.Label(root, text="", font=("Arial", 11))
sub_result_label.pack(pady=5)

# Chạy chương trình
root.mainloop()
