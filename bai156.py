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

root156.mainloop()
