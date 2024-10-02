import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, book_id, title, author, quantity=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
    
    def display(self):
        print(f"ID: {self.book_id}\nTen sach: {self.title}\nTac gia: {self.author}\nCo san: {self.quantity}")

    # Hàm cập nhật thông tin sách trên giao diện tkinter
    def update_info_gui(self):
        # Tạo cửa sổ cập nhật thông tin sách
        window = tk.Toplevel()
        window.title("Sua Thong Tin Sach")

        # Hiển thị thông tin hiện tại
        lbl_info = tk.Label(window, text="Thong tin hien tai cua sach:")
        lbl_info.grid(row=0, column=0, columnspan=2, pady=5)

        lbl_id = tk.Label(window, text=f"ID: {self.book_id}")
        lbl_id.grid(row=1, column=0, columnspan=2, pady=5)

        lbl_ten = tk.Label(window, text=f"Ten: {self.title}")
        lbl_ten.grid(row=2, column=0, columnspan=2, pady=5)

        lbl_tacgia = tk.Label(window, text=f"Tac gia: {self.author}")
        lbl_tacgia.grid(row=3, column=0, columnspan=2, pady=5)

        lbl_sl = tk.Label(window, text=f"So luong: {self.quantity}")
        lbl_sl.grid(row=4, column=0, columnspan=2, pady=5)

        # Các trường nhập liệu để cập nhật thông tin
        lbl_new_id = tk.Label(window, text="ID moi:")
        lbl_new_id.grid(row=5, column=0)
        entry_new_id = tk.Entry(window)
        entry_new_id.grid(row=5, column=1)
        entry_new_id.insert(0, str(self.book_id))  # Gán giá trị hiện tại

        lbl_new_ten = tk.Label(window, text="Ten moi:")
        lbl_new_ten.grid(row=6, column=0)
        entry_new_ten = tk.Entry(window)
        entry_new_ten.grid(row=6, column=1)
        entry_new_ten.insert(0, self.title)

        lbl_new_tacgia = tk.Label(window, text="Tac gia moi:")
        lbl_new_tacgia.grid(row=7, column=0)
        entry_new_tacgia = tk.Entry(window)
        entry_new_tacgia.grid(row=7, column=1)
        entry_new_tacgia.insert(0, self.author)

        lbl_new_sl = tk.Label(window, text="So luong moi:")
        lbl_new_sl.grid(row=8, column=0)
        entry_new_sl = tk.Entry(window)
        entry_new_sl.grid(row=8, column=1)
        entry_new_sl.insert(0, str(self.quantity))

        # Hàm lưu thông tin cập nhật
        def save_update():
            try:
                # Lấy giá trị mới từ các trường nhập liệu, nếu không nhập thì giữ nguyên giá trị cũ
                new_id_str = entry_new_id.get().strip()
                new_id = self.book_id if new_id_str == "" else int(new_id_str)

                new_title = entry_new_ten.get().strip()
                new_title = self.title if new_title == "" else new_title

                new_author = entry_new_tacgia.get().strip()
                new_author = self.author if new_author == "" else new_author

                new_quantity_str = entry_new_sl.get().strip()
                new_quantity = self.quantity if new_quantity_str == "" else int(new_quantity_str)

                # Cập nhật thuộc tính của đối tượng sách
                self.book_id = new_id
                self.title = new_title
                self.author = new_author
                self.quantity = new_quantity

                messagebox.showinfo("Thong bao", "Da cap nhat thong tin sach thanh cong!")
                window.destroy()

            except ValueError:
                messagebox.showerror("Loi", "Vui long nhap so nguyen hop le cho ID va so luong.")

        # Nút để lưu thông tin cập nhật
        btn_save = tk.Button(window, text="Luu", command=save_update)
        btn_save.grid(row=9, column=0, pady=10)

        # Nút để hủy bỏ và đóng cửa sổ mà không lưu
        def cancel_update():
            window.destroy()

        btn_cancel = tk.Button(window, text="Cancel", command=cancel_update)
        btn_cancel.grid(row=9, column=1, pady=10)

