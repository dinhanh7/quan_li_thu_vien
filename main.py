import tkinter as tk
from tkinter import ttk  # Import Treeview từ ttk
from tkinter import messagebox
from library import Library
from book import Book
from member import Member

# Khởi tạo đối tượng Library
library = Library()

# Đọc dữ liệu từ file sách và thành viên
def load_books():
    try:
        with open("book.txt", "r") as file:
            for line in file:
                book_id, title, author, quantity = line.strip().split(",")
                book = Book(int(book_id), title, author, int(quantity))
                library.add_book(book)
    except FileNotFoundError:
        pass  # Nếu file không tồn tại, bỏ qua

def load_members():
    try:
        with open("member.txt", "r") as file:
            for line in file:
                member_id, name, phone = line.strip().split(",")
                member = Member(member_id, name, phone)
                library.add_member(member)
    except FileNotFoundError:
        pass

# Đọc dữ liệu mượn từ file library.txt
def load_borrowed_books():
    try:
        with open("library.txt", "r") as file:
            for line in file:
                member_id, book_id, quantity = line.strip().split(",")
                if member_id not in library.borrowed_books:
                    library.borrowed_books[member_id] = {}
                library.borrowed_books[member_id][int(book_id)] = int(quantity)
    except FileNotFoundError:
        pass

# Ghi dữ liệu sách và thành viên vào file
def save_books():
    with open("book.txt", "w") as file:
        for book in library.books.values():
            file.write(f"{book.book_id},{book.title},{book.author},{book.quantity}\n")

def save_members():
    with open("member.txt", "w") as file:
        for member in library.members.values():
            file.write(f"{member.member_id},{member.name},{member.phone_number}\n")

# Ghi dữ liệu mượn vào file library.txt
def save_borrowed_books():
    with open("library.txt", "w") as file:
        for member_id, books in library.borrowed_books.items():
            for book_id, quantity in books.items():
                file.write(f"{member_id},{book_id},{quantity}\n")

# Hàm thêm sách
def add_book_gui():
    window = tk.Toplevel()
    window.title("Thêm sách")

    lbl_id = tk.Label(window, text="ID sách:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    lbl_title = tk.Label(window, text="Tên sách:")
    lbl_title.grid(row=1, column=0)
    entry_title = tk.Entry(window)
    entry_title.grid(row=1, column=1)

    lbl_author = tk.Label(window, text="Tác giả:")
    lbl_author.grid(row=2, column=0)
    entry_author = tk.Entry(window)
    entry_author.grid(row=2, column=1)

    lbl_quantity = tk.Label(window, text="Số lượng:")
    lbl_quantity.grid(row=3, column=0)
    entry_quantity = tk.Entry(window)
    entry_quantity.grid(row=3, column=1)

    def save_book():
        try:
            book_id = int(entry_id.get())
            title = entry_title.get()
            author = entry_author.get()
            quantity = int(entry_quantity.get())
            book = Book(book_id, title, author, quantity)
            library.add_book(book)
            save_books()  # Lưu vào file sau khi thêm sách
            window.destroy()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID và số lượng hợp lệ.")

    btn_save = tk.Button(window, text="Lưu", command=save_book)
    btn_save.grid(row=4, column=0, columnspan=2)

# Hàm xóa sách
def remove_book_gui():
    window = tk.Toplevel()
    window.title("Xóa sách")

    lbl_id = tk.Label(window, text="ID sách:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    def remove_book():
        try:
            book_id = int(entry_id.get())
            library.remove_book(book_id)
            save_books()  # Lưu vào file sau khi xóa sách
            window.destroy()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID hợp lệ.")

    btn_remove = tk.Button(window, text="Xóa", command=remove_book)
    btn_remove.grid(row=1, column=0, columnspan=2)

# Hàm cập nhật sách
def update_book_gui():
    window = tk.Toplevel()
    window.title("Cập nhật sách")

    lbl_id = tk.Label(window, text="ID sách:")
    lbl_id.grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    def update_book():
        try:
            book_id = int(entry_id.get())
            library.update_book(book_id)
            save_books()  # Lưu vào file sau khi cập nhật sách
            window.destroy()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID hợp lệ.")

    btn_update = tk.Button(window, text="Cập nhật", command=update_book)
    btn_update.grid(row=1, column=0, columnspan=2)

# Hiển thị sách dạng bảng
def display_books_gui():
    window = tk.Toplevel()
    window.title("Danh sách sách")

    # Tạo bảng Treeview
    tree = ttk.Treeview(window, columns=("ID", "Tên", "Tác giả", "Số lượng"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    # Đặt tên cột
    tree.heading("ID", text="ID")
    tree.heading("Tên", text="Tên")
    tree.heading("Tác giả", text="Tác giả")
    tree.heading("Số lượng", text="Số lượng")

    # Đặt kích thước cột
    tree.column("ID", width=50)
    tree.column("Tên", width=200)
    tree.column("Tác giả", width=150)
    tree.column("Số lượng", width=100)

    # Thêm dữ liệu sách vào bảng
    for book in library.books.values():
        tree.insert("", tk.END, values=(book.book_id, book.title, book.author, book.quantity))

# Hiển thị thành viên dạng bảng
def display_members_gui():
    window = tk.Toplevel()
    window.title("Danh sách thành viên")

    # Tạo bảng Treeview
    tree = ttk.Treeview(window, columns=("MSSV", "Tên", "Số điện thoại"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    # Đặt tên cột
    tree.heading("MSSV", text="MSSV")
    tree.heading("Tên", text="Tên")
    tree.heading("Số điện thoại", text="Số điện thoại")

    # Đặt kích thước cột
    tree.column("MSSV", width=100)
    tree.column("Tên", width=200)
    tree.column("Số điện thoại", width=150)

    # Thêm dữ liệu thành viên vào bảng
    for member in library.members.values():
        tree.insert("", tk.END, values=(member.member_id, member.name, member.phone_number))

# Hàm thêm thành viên
def add_member_gui():
    window = tk.Toplevel()
    window.title("Thêm thành viên")

    lbl_mssv = tk.Label(window, text="MSSV:")
    lbl_mssv.grid(row=0, column=0)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=0, column=1)

    lbl_name = tk.Label(window, text="Tên:")
    lbl_name.grid(row=1, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=1, column=1)

    lbl_phone = tk.Label(window, text="Số điện thoại:")
    lbl_phone.grid(row=2, column=0)
    entry_phone = tk.Entry(window)
    entry_phone.grid(row=2, column=1)

    def save_member():
        mssv = entry_mssv.get()
        name = entry_name.get()
        phone = entry_phone.get()
        member = Member(mssv, name, phone)
        library.add_member(member)
        save_members()  # Lưu vào file sau khi thêm thành viên
        window.destroy()

    btn_save = tk.Button(window, text="Lưu", command=save_member)
    btn_save.grid(row=3, column=0, columnspan=2)

# Hàm xóa thành viên
def remove_member_gui():
    window = tk.Toplevel()
    window.title("Xóa thành viên")

    lbl_mssv = tk.Label(window, text="MSSV:")
    lbl_mssv.grid(row=0, column=0)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=0, column=1)

    def remove_member():
        mssv = entry_mssv.get()
        library.remove_member(mssv)
        save_members()  # Lưu vào file sau khi xóa thành viên
        window.destroy()

    btn_remove = tk.Button(window, text="Xóa", command=remove_member)
    btn_remove.grid(row=1, column=0, columnspan=2)

# Hàm cập nhật thành viên
def update_member_gui():
    window = tk.Toplevel()
    window.title("Cập nhật thành viên")

    lbl_mssv = tk.Label(window, text="MSSV:")
    lbl_mssv.grid(row=0, column=0)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=0, column=1)

    def update_member():
        mssv = entry_mssv.get()
        library.update_member(mssv)
        save_members()  # Lưu vào file sau khi cập nhật thành viên
        window.destroy()

    btn_update = tk.Button(window, text="Cập nhật", command=update_member)
    btn_update.grid(row=1, column=0, columnspan=2)

# Hàm mượn sách
def borrow_book_gui():
    window = tk.Toplevel()
    window.title("Mượn sách")

    lbl_mssv = tk.Label(window, text="MSSV thành viên:")
    lbl_mssv.grid(row=0, column=0)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=0, column=1)

    lbl_book_id = tk.Label(window, text="ID sách:")
    lbl_book_id.grid(row=1, column=0)
    entry_book_id = tk.Entry(window)
    entry_book_id.grid(row=1, column=1)

    lbl_quantity = tk.Label(window, text="Số lượng mượn:")
    lbl_quantity.grid(row=2, column=0)
    entry_quantity = tk.Entry(window)
    entry_quantity.grid(row=2, column=1)

    def borrow_book():
        mssv = entry_mssv.get()
        try:
            book_id = int(entry_book_id.get())
            quantity = int(entry_quantity.get())
            library.borrow_book(mssv, book_id, quantity)
            save_books()  # Cập nhật số lượng sách
            save_borrowed_books()  # Lưu dữ liệu mượn vào file
            window.destroy()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID và số lượng hợp lệ.")

    btn_borrow = tk.Button(window, text="Mượn", command=borrow_book)
    btn_borrow.grid(row=3, column=0, columnspan=2)

# Hàm trả sách
def return_book_gui():
    window = tk.Toplevel()
    window.title("Trả sách")

    lbl_mssv = tk.Label(window, text="MSSV thành viên:")
    lbl_mssv.grid(row=0, column=0)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=0, column=1)

    lbl_book_id = tk.Label(window, text="ID sách:")
    lbl_book_id.grid(row=1, column=0)
    entry_book_id = tk.Entry(window)
    entry_book_id.grid(row=1, column=1)

    lbl_quantity = tk.Label(window, text="Số lượng trả:")
    lbl_quantity.grid(row=2, column=0)
    entry_quantity = tk.Entry(window)
    entry_quantity.grid(row=2, column=1)

    def return_book():
        mssv = entry_mssv.get()
        try:
            book_id = int(entry_book_id.get())
            quantity = int(entry_quantity.get())
            library.return_book(mssv, book_id, quantity)
            save_books()  # Cập nhật số lượng sách
            save_borrowed_books()  # Lưu dữ liệu mượn vào file
            window.destroy()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID và số lượng hợp lệ.")

    btn_return = tk.Button(window, text="Trả", command=return_book)
    btn_return.grid(row=3, column=0, columnspan=2)

# Hiển thị sách thành viên đang mượn
def display_member_borrowing_gui():
    window = tk.Toplevel()
    window.title("Sách thành viên đang mượn")

    lbl_mssv = tk.Label(window, text="MSSV thành viên:")
    lbl_mssv.grid(row=0, column=0)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=0, column=1)

    def display_borrowing():
        mssv = entry_mssv.get()
        if mssv in library.borrowed_books:
            text_box = tk.Text(window)
            text_box.grid(row=2, column=0, columnspan=2)
            for book_id in library.borrowed_books[mssv]:
                if book_id in library.books:
                    book = library.books[book_id]
                    text_box.insert(tk.END, f"ID: {book.book_id}, Tên: {book.title}, Số lượng: {library.borrowed_books[mssv][book_id]}\n")
        else:
            messagebox.showinfo("Thông báo", "Thành viên không mượn sách nào.")

    btn_display = tk.Button(window, text="Hiển thị", command=display_borrowing)
    btn_display.grid(row=1, column=0, columnspan=2)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thư viện quản lý")

# Nhóm chức năng Quản lý sách
frame_books = tk.LabelFrame(root, text="Chức năng Quản lý sách")
frame_books.pack(padx=10, pady=10, fill="both")

btn_add_book = tk.Button(frame_books, text="Thêm sách", command=add_book_gui)
btn_add_book.pack(padx=5, pady=5)

btn_remove_book = tk.Button(frame_books, text="Xóa sách", command=remove_book_gui)
btn_remove_book.pack(padx=5, pady=5)

btn_update_book = tk.Button(frame_books, text="Cập nhật sách", command=update_book_gui)
btn_update_book.pack(padx=5, pady=5)

btn_display_books = tk.Button(frame_books, text="Hiển thị sách", command=display_books_gui)
btn_display_books.pack(padx=5, pady=5)

# Nhóm chức năng Quản lý thành viên
frame_members = tk.LabelFrame(root, text="Chức năng Quản lý thành viên")
frame_members.pack(padx=10, pady=10, fill="both")

btn_add_member = tk.Button(frame_members, text="Thêm thành viên", command=add_member_gui)
btn_add_member.pack(padx=5, pady=5)

btn_remove_member = tk.Button(frame_members, text="Xóa thành viên", command=remove_member_gui)
btn_remove_member.pack(padx=5, pady=5)

btn_update_member = tk.Button(frame_members, text="Cập nhật thành viên", command=update_member_gui)
btn_update_member.pack(padx=5, pady=5)

btn_display_members = tk.Button(frame_members, text="Hiển thị thành viên", command=display_members_gui)
btn_display_members.pack(padx=5, pady=5)

# Nhóm chức năng Mượn trả sách
frame_borrow_return = tk.LabelFrame(root, text="Chức năng Mượn/Trả sách")
frame_borrow_return.pack(padx=10, pady=10, fill="both")

btn_borrow_book = tk.Button(frame_borrow_return, text="Mượn sách", command=borrow_book_gui)
btn_borrow_book.pack(padx=5, pady=5)

btn_return_book = tk.Button(frame_borrow_return, text="Trả sách", command=return_book_gui)
btn_return_book.pack(padx=5, pady=5)

btn_display_borrowing = tk.Button(frame_borrow_return, text="Hiển thị sách thành viên đang mượn", command=display_member_borrowing_gui)
btn_display_borrowing.pack(padx=5, pady=5)

# Khởi động chương trình và tải dữ liệu từ file
load_books()
load_members()
load_borrowed_books()

# Bắt đầu vòng lặp chính
root.mainloop()
