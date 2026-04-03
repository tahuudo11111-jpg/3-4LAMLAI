import tkinter as tk

def split_list():
    raw = entry_list.get().strip()
    if not raw: return
    
    try:
        # Chuyển chuỗi thành list, bỏ số 0 ở cuối nếu có theo đề bài
        full_list = [int(x) for x in raw.split() if x != '0']
        
        list_chan = [x for x in full_list if x % 2 == 0]
        list_le = [x for x in full_list if x % 2 != 0]
        
        # Đảo ngược như trong ảnh mẫu (nếu bạn muốn giống hệt ảnh)
        list_chan.reverse()
        list_le.reverse()
        
        res = f"List gốc : {' '.join(f'[{x}]' for x in full_list)}\n"
        res += f"List chẵn (đảo): {' '.join(f'[{x}]' for x in list_chan)}\n"
        res += f"List lẻ   (đảo): {' '.join(f'[{x}]' for x in list_le)}"
        
        lbl_display.config(text=res)
    except:
        lbl_display.config(text="Dữ liệu nhập không hợp lệ!")

root207 = tk.Tk()
root207.title("Bài 207 - Tách Liên Kết Đơn")
root207.geometry("500x300")

tk.Label(root207, text="Nhập dãy số (kết thúc bằng 0):", font=("Arial", 11)).pack(pady=10)
entry_list = tk.Entry(root207, width=40, font=("Consolas", 12))
entry_list.pack(pady=5)
entry_list.insert(0, "1 2 3 4 5 6 7 8 0")

tk.Button(root207, text="Tách Chẵn Lẻ", command=split_list, bg="#607D8B", fg="white").pack(pady=15)

lbl_display = tk.Label(root207, text="", font=("Consolas", 11), justify="left")
lbl_display.pack(pady=10)

root207.mainloop()
