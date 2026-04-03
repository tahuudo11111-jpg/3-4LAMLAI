import tkinter as tk
from tkinter import messagebox
import random

def solve_bai106():
    try:
        n = int(entry_n.get())
        if n <= 0:
            messagebox.showwarning("Lỗi", "n phải > 0")
            return
        
        matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        
        txt_result.delete(1.0, tk.END)
        txt_result.insert(tk.END, "Ma trận được tạo:\n")
        for row in matrix:
            txt_result.insert(tk.END, " ".join(f"{x:3d}" for x in row) + "\n")
            
        txt_result.insert(tk.END, "\nCác điểm yên ngựa:\n")
        found = False
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                row = matrix[i]
                col = [matrix[k][j] for k in range(n)]
                
                if (val == min(row) and val == max(col)) or (val == max(row) and val == min(col)):
                    txt_result.insert(tk.END, f"A[{i}][{j}] = {val}\n")
                    found = True
                    
        if not found:
            txt_result.insert(tk.END, "Không có điểm yên ngựa nào.")
            
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập bậc ma trận (số nguyên)!")

root106 = tk.Tk()
root106.title("Bài 106 - Điểm Yên Ngựa")
root106.geometry("400x400")

tk.Label(root106, text="Nhập bậc ma trận n:").pack(pady=10)
entry_n = tk.Entry(root106, width=15)
entry_n.pack(pady=5)

tk.Button(root106, text="Tạo & Tìm Điểm", command=solve_bai106, bg="#FF9800", fg="white").pack(pady=10)

txt_result = tk.Text(root106, height=15, width=45)
txt_result.pack(pady=5)

root106.mainloop()
