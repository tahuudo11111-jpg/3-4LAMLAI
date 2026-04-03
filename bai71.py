import tkinter as tk
from tkinter import messagebox

def solve_bai71():
    try:
        arr_str = entry_arr.get().strip()
        k = int(entry_k.get())
        
        if not arr_str:
            messagebox.showwarning("Lỗi", "Vui lòng nhập mảng!")
            return
            
        arr = list(map(int, arr_str.split()))
        
        # Kiểm tra đối xứng
        is_sym = "Mảng Đối xứng" if arr == arr[::-1] else "Mảng Không đối xứng"
        
        # Dịch trái xoay vòng k lần
        n = len(arr)
        k = k % n
        shifted_arr = arr[k:] + arr[:k]
        
        txt_result.delete(1.0, tk.END)
        txt_result.insert(tk.END, f"Kết quả kiểm tra: {is_sym}\n\n")
        txt_result.insert(tk.END, f"Mảng sau khi dịch trái {k} lần:\n")
        txt_result.insert(tk.END, " ".join(map(str, shifted_arr)))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số liệu hợp lệ!")

root71 = tk.Tk()
root71.title("Bài 71 - Mảng 1 chiều")
root71.geometry("400x350")

tk.Label(root71, text="Nhập mảng (cách nhau bởi dấu cách):").pack(pady=10)
entry_arr = tk.Entry(root71, width=40)
entry_arr.pack(pady=5)

tk.Label(root71, text="Nhập số lần dịch trái k:").pack(pady=10)
entry_k = tk.Entry(root71, width=10)
entry_k.pack(pady=5)

tk.Button(root71, text="Thực hiện", command=solve_bai71, bg="#4CAF50", fg="white").pack(pady=15)

txt_result = tk.Text(root71, height=8, width=45)
txt_result.pack(pady=5)

root71.mainloop()
