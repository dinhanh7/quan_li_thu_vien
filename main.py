import tkinter as tk
from tkinter import messagebox
from library import Library, Book, Member

# Tao doi tuong thu vien
library = Library()

# Ham cho cac chuc nang quan ly thu vien
def them_sach():
    window = tk.Toplevel(root)
    window.title("Them Sach")

    lbl_id = tk.Label(window, text="ID Sach:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    lbl_ten = tk.Label(window, text="Ten Sach:")
    lbl_ten.grid(row=1, column=0)
    entry_ten = tk.Entry(window)
    entry_ten.grid(row=1, column=1)

    lbl_tacgia = tk.Label(window, text="Tac Gia:")
    lbl_tacgia.grid(row=2, column=0)
    entry_tacgia = tk.Entry(window)
    entry_tacgia.grid(row=2, column=1)

    lbl_sl = tk.Label(window, text="So Luong:")
    lbl_sl.grid(row=3, column=0)
    entry_sl = tk.Entry(window)
    entry_sl.grid(row=3, column=1)

    def luu_sach():
        book_id = int(entry_id.get())
        title = entry_ten.get()
        author = entry_tacgia.get()
        quantity = int(entry_sl.get())
        library.books[book_id] = Book(book_id, title, author, quantity)
        messagebox.showinfo("Thong bao", f"Da them sach {title}")
        window.destroy()

    btn_luu = tk.Button(window, text="Luu", command=luu_sach)
    btn_luu.grid(row=4, column=1)

def sua_sach():
    window = tk.Toplevel(root)
    window.title("Sua Thong Tin Sach")

    lbl_id = tk.Label(window, text="Nhap ID sach de sua:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    def sua():
        book_id = int(entry_id.get())
        if book_id in library.books:
            book = library.books[book_id]
            book.update_info()
            messagebox.showinfo("Thong bao", "Da sua thong tin sach.")
        else:
            messagebox.showwarning("Thong bao", "Khong tim thay sach voi ID nay.")
        window.destroy()

    btn_sua = tk.Button(window, text="Sua", command=sua)
    btn_sua.grid(row=1, column=1)

def hien_thi_sach():
    window = tk.Toplevel(root)
    window.title("Danh sach sach")

    if not library.books:
        lbl_thongbao = tk.Label(window, text="Thu vien khong co sach nao.")
        lbl_thongbao.pack()
    else:
        for book in library.books.values():
            lbl_sach = tk.Label(window, text=f"ID: {book.book_id} - Ten: {book.title} - Tac Gia: {book.author} - So Luong: {book.quantity}")
            lbl_sach.pack()

def them_thanh_vien():
    window = tk.Toplevel(root)
    window.title("Them Thanh Vien")

    lbl_id = tk.Label(window, text="MSSV:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    lbl_ten = tk.Label(window, text="Ten Thanh Vien:")
    lbl_ten.grid(row=1, column=0)
    entry_ten = tk.Entry(window)
    entry_ten.grid(row=1, column=1)

    lbl_phone = tk.Label(window, text="So Dien Thoai:")
    lbl_phone.grid(row=2, column=0)
    entry_phone = tk.Entry(window)
    entry_phone.grid(row=2, column=1)

    def luu_thanh_vien():
        member_id = entry_id.get()
        name = entry_ten.get()
        phone = entry_phone.get()
        library.members[member_id] = Member(member_id, name, phone)
        library.borrowed_books[member_id] = []
        messagebox.showinfo("Thong bao", f"Da them thanh vien {name}")
        window.destroy()

    btn_luu = tk.Button(window, text="Luu", command=luu_thanh_vien)
    btn_luu.grid(row=3, column=1)

def sua_thanh_vien():
    window = tk.Toplevel(root)
    window.title("Sua Thong Tin Thanh Vien")

    lbl_id = tk.Label(window, text="Nhap MSSV de sua:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    def sua():
        member_id = entry_id.get()
        if member_id in library.members:
            member = library.members[member_id]
            member.update_info(member_id, member.name, member.phone_number)
            messagebox.showinfo("Thong bao", "Da sua thong tin thanh vien.")
        else:
            messagebox.showwarning("Thong bao", "Khong tim thay thanh vien voi MSSV nay.")
        window.destroy()

    btn_sua = tk.Button(window, text="Sua", command=sua)
    btn_sua.grid(row=1, column=1)

def xoa_thanh_vien():
    window = tk.Toplevel(root)
    window.title("Xoa Thanh Vien")

    lbl_id = tk.Label(window, text="Nhap MSSV thanh vien de xoa:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    def xac_nhan_xoa():
        member_id = entry_id.get()
        if member_id in library.members:
            del library.members[member_id]
            del library.borrowed_books[member_id]
            messagebox.showinfo("Thong bao", "Da xoa thanh vien khoi he thong.")
        else:
            messagebox.showwarning("Thong bao", "Khong tim thay thanh vien voi MSSV nay.")
        window.destroy()

    btn_xoa = tk.Button(window, text="Xoa", command=xac_nhan_xoa)
    btn_xoa.grid(row=1, column=1)

def muon_sach():
    window = tk.Toplevel(root)
    window.title("Muon Sach")

    lbl_id_tv = tk.Label(window, text="MSSV Thanh Vien:")
    lbl_id_tv.grid(row=0, column=0)
    entry_id_tv = tk.Entry(window)
    entry_id_tv.grid(row=0, column=1)

    lbl_id_sach = tk.Label(window, text="ID Sach:")
    lbl_id_sach.grid(row=1, column=0)
    entry_id_sach = tk.Entry(window)
    entry_id_sach.grid(row=1, column=1)

    def xac_nhan_muon():
        member_id = entry_id_tv.get()
        book_id = int(entry_id_sach.get())
        library.borrow_book(member_id, book_id)
        window.destroy()

    btn_muon = tk.Button(window, text="Muon", command=xac_nhan_muon)
    btn_muon.grid(row=2, column=1)

def tra_sach():
    window = tk.Toplevel(root)
    window.title("Tra Sach")

    lbl_id_tv = tk.Label(window, text="MSSV Thanh Vien:")
    lbl_id_tv.grid(row=0, column=0)
    entry_id_tv = tk.Entry(window)
    entry_id_tv.grid(row=0, column=1)

    lbl_id_sach = tk.Label(window, text="ID Sach:")
    lbl_id_sach.grid(row=1, column=0)
    entry_id_sach = tk.Entry(window)
    entry_id_sach.grid(row=1, column=1)

    def xac_nhan_tra():
        member_id = entry_id_tv.get()
        book_id = int(entry_id_sach.get())
        library.return_book(member_id, book_id)
        window.destroy()

    btn_tra = tk.Button(window, text="Tra", command=xac_nhan_tra)
    btn_tra.grid(row=2, column=1)

def hien_thi_thong_tin_sach_muon():
    window = tk.Toplevel(root)
    window.title("Thong Tin Sach Dang Muon")

    lbl_id = tk.Label(window, text="Nhap MSSV thanh vien:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    def hien_thi():
        member_id = entry_id.get()
        library.display_member_borrowing(member_id)

    btn_hien_thi = tk.Button(window, text="Hien Thi", command=hien_thi)
    btn_hien_thi.grid(row=1, column=1)

def hien_thi_tong_hop_muon_sach():
    window = tk.Toplevel(root)
    window.title("Tong Hop Muon Sach")

    library.display_borrowing_summary()

# Tao cua so chinh
root = tk.Tk()
root.title("Quan Ly Thu Vien")

# Them cac nut chuc nang
btn_muon_sach = tk.Button(root, text="Muon Sach", command=muon_sach)
btn_muon_sach.pack(pady=5)

btn_tra_sach = tk.Button(root, text="Tra Sach", command=tra_sach)
btn_tra_sach.pack(pady=5)

btn_thong_tin_sach_muon = tk.Button(root, text="Thong Tin Sach Dang Muon", command=hien_thi_thong_tin_sach_muon)
btn_thong_tin_sach_muon.pack(pady=5)

btn_tong_hop_muon_sach = tk.Button(root, text="Tong Hop Muon Sach", command=hien_thi_tong_hop_muon_sach)
btn_tong_hop_muon_sach.pack(pady=5)

btn_hien_thi_sach = tk.Button(root, text="Hien Thi Tat Ca Sach", command=hien_thi_sach)
btn_hien_thi_sach.pack(pady=5)

btn_them_sach = tk.Button(root, text="Them Sach", command=them_sach)
btn_them_sach.pack(pady=5)

btn_sua_sach = tk.Button(root, text="Sua Thong Tin Sach", command=sua_sach)
btn_sua_sach.pack(pady=5)

btn_hien_thi_tv = tk.Button(root, text="Hien Thi Tat Ca Thanh Vien", command=hien_thi_thong_tin_sach_muon)
btn_hien_thi_tv.pack(pady=5)

btn_them_tv = tk.Button(root, text="Them Thanh Vien", command=them_thanh_vien)
btn_them_tv.pack(pady=5)

btn_sua_tv = tk.Button(root, text="Sua Thong Tin Thanh Vien", command=sua_thanh_vien)
btn_sua_tv.pack(pady=5)

btn_xoa_tv = tk.Button(root, text="Xoa Thanh Vien", command=xoa_thanh_vien)
btn_xoa_tv.pack(pady=5)

# Chay giao dien
root.mainloop()
