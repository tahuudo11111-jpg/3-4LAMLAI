import tkinter as tk

def calc_fraction(x):
    # Điểm dừng của đệ quy là khi mẫu số đạt 103
    if x == 103:
        return 103.0
    return x + 1.0 / calc_fraction(x + 2)

def solve_bai156():
    # Bắt đầu đệ quy từ số 1
    result = calc_fraction(1)
    lbl_result.config(text=f"F = {result:.5f}")

root156 = tk.Tk()
root156.title("Bài 156 - Phân Số Liên Tục")
root156.geometry("350x200")

tk.Label(root156, text="Tính phân số liên tục bằng hàm đệ quy", font=("Arial", 11)).pack(pady=20)

tk.Button(root156, text="Tính Kết Quả", command=solve_bai156, font=("Arial", 10, "bold"), bg="#009688", fg="white").pack(pady=10)

lbl_result = tk.Label(root156, text="F = ---", font=("Consolas", 14, "bold"), fg="red")
lbl_result.pack(pady=20)

root156.mainloop()/-strong/-heart:>:o:-((:-h 156/-strong/-heart:>:o:-((:-h import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bài 168 - Quản lý sách")
        self.root.geometry("500x500")
        self.books = []

        # Form nhập liệu
        fields = ["Tựa sách", "ISBN", "Tác giả", "NXB"]
        self.entries = {}
        for field in fields:
            frame = tk.Frame(root)
            frame.pack(pady=5, padx=20, fill='x')
            tk.Label(frame, text=field, width=10, anchor='w').pack(side='left')
            entry = tk.Entry(frame)
            entry.pack(side='right', expand=True, fill='x')
            self.entries[field] = entry

        tk.Button(root, text="Thêm Sách", command=self.add_book, bg="#4CAF50", fg="white").pack(pady=10)
        
        # Form tìm kiếm
        tk.Label(root, text="Nhập ISBN để tìm:").pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack(pady=5)
        tk.Button(root, text="Tìm kiếm", command=self.search_book, bg="#2196F3", fg="white").pack()

        self.txt_display = tk.Text(root, height=10, width=55)
        self.txt_display.pack(pady=10)

    def add_book(self):
        data = {k: v.get() for k, v in self.entries.items()}
        if not data["ISBN"]: return
        data["date"] = datetime.now().strftime("%d-%m-%Y")
        self.books.append(data)
        messagebox.showinfo("Thành công", f"Đã thêm: {data['Tựa sách']}")
        for e in self.entries.values(): e.delete(0, tk.END)

    def search_book(self):
        isbn = self.search_entry.get()
        self.txt_display.delete(1.0, tk.END)
        for b in self.books:
            if b["ISBN"] == isbn:
                res = f"Kết quả tìm:\n{b['Tựa sách']}\n{b['Tác giả']}\n{b['NXB']}\n[update: {b['date']}]"
                self.txt_display.insert(tk.END, res)
                return
        self.txt_display.insert(tk.END, "Không tìm thấy sách!")

root168 = tk.Tk(); app = BookApp(root168); root168.mainloop()
