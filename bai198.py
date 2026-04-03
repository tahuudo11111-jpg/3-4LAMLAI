import tkinter as tk

def get_bytes():
    try:
        n = int(entry_n.get())
        # Giả định n là 32-bit (unsigned long tương đương)
        high = (n >> 16) & 0xFFFF
        low = n & 0xFFFF
        
        res = f"Số thập phân: {n}\n"
        res += f"Nhị phân: {bin(n)[2:].zfill(32)}\n\n"
        res += f"High Byte (16-bit cao): {high} = {bin(high)[2:].zfill(16)}\n"
        res += f"Low Byte  (16-bit thấp): {low} = {bin(low)[2:].zfill(16)}"
        
        lbl_res.config(text=res)
    except:
        lbl_res.config(text="Vui lòng nhập số nguyên!")

root198 = tk.Tk()
root198.title("Bài 198 - High/Low Byte 32-bit")
root198.geometry("450x300")

tk.Label(root198, text="Nhập số integer n:").pack(pady=10)
entry_n = tk.Entry(root198, font=("Consolas", 12))
entry_n.pack()
tk.Button(root198, text="Trích xuất Byte", command=get_bytes, bg="#FF5722", fg="white").pack(pady=10)

lbl_res = tk.Label(root198, text="", font=("Consolas", 10), justify="left")
lbl_res.pack(pady=10)

root198.mainloop()
