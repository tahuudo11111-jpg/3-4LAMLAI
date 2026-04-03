import tkinter as tk
from tkinter import messagebox

def insert_descending(arr, val):
    for i in range(len(arr)):
        if val > arr[i]:
            arr.insert(i, val)
            return
    arr.append(val)

def solve_bai84():
    try:
        arr_str = entry_arr.get().strip()
        if not arr_str:
            messagebox.showwarning("Lỗi", "Vui lòng nhập số liệu!")
            return
        
        input_nums = list(map(int, arr_str.split()))
        sorted_arr = []
        for num in input_nums:
            insert_descending(sorted_arr, num)
            
        lbl_result.config(text=f"Mảng đã sắp xếp: {' '.join(map(str, sorted_arr))}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập các số nguyên hợp lệ!")

root84 = tk.Tk()
root84.title("Bài 84 - Mảng Giảm Dần")
root84.geometry("400x200")

tk.Label(root84, text="Nhập dãy số (cách nhau bởi dấu cách):").pack(pady=15)
entry_arr = tk.Entry(root84, width=50)
entry_arr.pack(pady=5)

tk.Button(root84, text="Chèn và Sắp xếp", command=solve_bai84, bg="#2196F3", fg="white").pack(pady=15)

lbl_result = tk.Label(root84, text="Mảng đã sắp xếp: ", font=("Arial", 11, "bold"))
lbl_result.pack(pady=5)

root84.mainloop()
