import tkinter as tk
from tkinter import messagebox

class Member:
    def __init__(self, mssv, name, phone):
        self.member_id = mssv
        self.name = name
        self.phone_number = phone

    def display(self):
        print(f"MSSV: {self.member_id}\nName: {self.name}\nPhone number: {self.phone_number}")

    # Hàm cập nhật thông tin thành viên trên giao diện tkinter
    def update_info_gui(self):
        # Tạo cửa sổ cập nhật thông tin thành viên
        window = tk.Toplevel()
        window.title("Sua Thong Tin Thanh Vien")

        # Hiển thị thông tin hiện tại
        lbl_info = tk.Label(window, text="Thong tin hien tai cua thanh vien:")
        lbl_info.grid(row=0, column=0, columnspan=2, pady=5)

        lbl_id = tk.Label(window, text=f"MSSV: {self.member_id}")
        lbl_id.grid(row=1, column=0, columnspan=2, pady=5)

        lbl_name = tk.Label(window, text=f"Ten: {self.name}")
        lbl_name.grid(row=2, column=0, columnspan=2, pady=5)

        lbl_phone = tk.Label(window, text=f"So dien thoai: {self.phone_number}")
        lbl_phone.grid(row=3, column=0, columnspan=2, pady=5)

        # Các trường nhập liệu để cập nhật thông tin
        lbl_new_id = tk.Label(window, text="MSSV moi:")
        lbl_new_id.grid(row=4, column=0)
        entry_new_id = tk.Entry(window)
        entry_new_id.grid(row=4, column=1)
        entry_new_id.insert(0, self.member_id)  # Gán giá trị hiện tại

        lbl_new_name = tk.Label(window, text="Ten moi:")
        lbl_new_name.grid(row=5, column=0)
        entry_new_name = tk.Entry(window)
        entry_new_name.grid(row=5, column=1)
        entry_new_name.insert(0, self.name)

        lbl_new_phone = tk.Label(window, text="So dien thoai moi:")
        lbl_new_phone.grid(row=6, column=0)
        entry_new_phone = tk.Entry(window)
        entry_new_phone.grid(row=6, column=1)
        entry_new_phone.insert(0, self.phone_number)

        # Hàm lưu thông tin cập nhật
        def save_update():
            # Lấy giá trị mới từ các trường nhập liệu, nếu không nhập thì giữ nguyên giá trị cũ
            new_id = entry_new_id.get().strip()
            new_id = self.member_id if new_id == "" else new_id

            new_name = entry_new_name.get().strip()
            new_name = self.name if new_name == "" else new_name

            new_phone = entry_new_phone.get().strip()
            new_phone = self.phone_number if new_phone == "" else new_phone

            # Cập nhật thuộc tính của đối tượng thành viên
            self.member_id = new_id
            self.name = new_name
            self.phone_number = new_phone

            messagebox.showinfo("Thong bao", "Da cap nhat thong tin thanh vien thanh cong!")
            window.destroy()

        # Nút để lưu thông tin cập nhật
        btn_save = tk.Button(window, text="Luu", command=save_update)
        btn_save.grid(row=7, column=0, pady=10)

        # Nút để hủy bỏ và đóng cửa sổ mà không lưu
        def cancel_update():
            window.destroy()

        btn_cancel = tk.Button(window, text="Cancel", command=cancel_update)
        btn_cancel.grid(row=7, column=1, pady=10)

