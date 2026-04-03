import tkinter as tk
from tkinter import messagebox

def solve_bai133():
    hex_str = entry_hex.get().strip().upper()
    if not hex_str:
        messagebox.showwarning("Lỗi", "Vui lòng nhập chuỗi Hex!")
        return
    
    try:
        x = 0
        for char in hex_str:
            val = int(char, 16)
            x = 16 * x + val
            
        lbl_result.config(text=f"Decimal: {x}")
    except ValueError:
        messagebox.showerror("Lỗi", "Chuỗi Hex chứa ký tự không hợp lệ!")

root133 = tk.Tk()
root133.title("Bài 133 - Hex to Dec")
root133.geometry("350x200")

tk.Label(root133, text="Nhập chuỗi số Hex:").pack(pady=15)
entry_hex = tk.Entry(root133, width=25, font=("Consolas", 12))
entry_hex.pack(pady=5)

tk.Button(root133, text="Chuyển đổi", command=solve_bai133, bg="#9C27B0", fg="white").pack(pady=10)

lbl_result = tk.Label(root133, text="Decimal: ---", font=("Arial", 12, "bold"))
lbl_result.pack(pady=10)

root133.mainloop()
