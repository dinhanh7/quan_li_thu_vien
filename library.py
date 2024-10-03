import tkinter as tk
from tkinter import messagebox
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}  # Sử dụng từ điển để quản lý sách (ID: Book)
        self.members = {}  # Sử dụng từ điển để quản lý thành viên (MSSV: Member)
        self.borrowed_books = {}  # Sử dụng từ điển để theo dõi sách đã mượn (MSSV: [book_id])

    def add_book(self, book):
        """Thêm sách vào thư viện."""
        if book.book_id in self.books:
            messagebox.showwarning("Warning", "Sách này đã tồn tại!")
        else:
            self.books[book.book_id] = book

    def remove_book(self, book_id):
        """Xóa sách khỏi thư viện."""
        if book_id in self.books:
            del self.books[book_id]
            messagebox.showinfo("Thông báo", "Sách đã được xóa thành công!")
        else:
            messagebox.showwarning("Warning", "Không tìm thấy sách với ID này!")

    def update_book(self, book_id):
        """Cập nhật thông tin sách."""
        if book_id in self.books:
            self.books[book_id].update_info_gui()
        else:
            messagebox.showwarning("Warning", "Không tìm thấy sách với ID này!")

    def add_member(self, member):
        """Thêm thành viên vào thư viện."""
        if member.member_id in self.members:
            messagebox.showwarning("Warning", "Thành viên này đã tồn tại!")
        else:
            self.members[member.member_id] = member

    def update_member(self, member_id):
        """Cập nhật thông tin thành viên."""
        if member_id in self.members:
            self.members[member_id].update_info_gui()
        else:
            messagebox.showwarning("Warning", "Không tìm thấy thành viên với MSSV này!")

    def remove_member(self, member_id):
        """Xóa thành viên khỏi thư viện."""
        if member_id in self.members:
            del self.members[member_id]
            messagebox.showinfo("Thông báo", "Thành viên đã được xóa thành công!")
        else:
            messagebox.showwarning("Warning", "Không tìm thấy thành viên với MSSV này!")

    def borrow_book(self, member_id, book_id, quantity=1):
        """Thành viên mượn sách với số lượng."""
        if member_id not in self.members:
            messagebox.showwarning("Warning", "Thành viên không tồn tại!")
            return

        if book_id not in self.books:
            messagebox.showwarning("Warning", "Sách không tồn tại!")
            return

        if self.books[book_id].quantity < quantity:
            messagebox.showwarning("Warning", "Không đủ số lượng sách để mượn!")
            return

        if member_id not in self.borrowed_books:
            self.borrowed_books[member_id] = {}
        
        if book_id not in self.borrowed_books[member_id]:
            self.borrowed_books[member_id][book_id] = 0
        
        self.borrowed_books[member_id][book_id] += quantity
        self.books[book_id].quantity -= quantity
        
        messagebox.showinfo("Thông báo", "Thành viên đã mượn sách thành công!")

    def return_book(self, member_id, book_id, quantity=1):
        """Thành viên trả sách với số lượng."""
        if member_id not in self.borrowed_books or book_id not in self.borrowed_books[member_id]:
            messagebox.showwarning("Warning", "Thành viên không mượn sách này!")
            return

        borrowed_quantity = self.borrowed_books[member_id][book_id]

        if borrowed_quantity < quantity:
            messagebox.showwarning("Warning", "Thành viên không mượn đủ số lượng sách để trả!")
            return

        # Update returned quantity
        self.borrowed_books[member_id][book_id] -= quantity
        if self.borrowed_books[member_id][book_id] == 0:
            del self.borrowed_books[member_id][book_id]

        self.books[book_id].quantity += quantity  # Increase available quantity
        messagebox.showinfo("Thông báo", "Thành viên đã trả sách thành công!")
    def return_book(self, member_id, book_id):
        """Thành viên trả sách."""
        if member_id not in self.borrowed_books or book_id not in self.borrowed_books[member_id]:
            messagebox.showwarning("Warning", "Thành viên không mượn sách này!")
            return

        self.borrowed_books[member_id].remove(book_id)
        self.books[book_id].quantity += 1
        messagebox.showinfo("Thông báo", "Thành viên đã trả sách thành công!")

    def display_books(self):
        """Hiển thị danh sách sách trong thư viện."""
        for book in self.books.values():
            book.display()

    def display_members(self):
        """Hiển thị danh sách thành viên trong thư viện."""
        for member in self.members.values():
            member.display()

    def display_member_borrowing(self, member_id):
        """Hiển thị thông tin sách mà thành viên đang mượn."""
        if member_id in self.borrowed_books:
            print(f"Thành viên {member_id} đang mượn các sách sau:")
            for book_id in self.borrowed_books[member_id]:
                if book_id in self.books:
                    self.books[book_id].display()
        else:
            print(f"Thành viên {member_id} hiện không mượn sách nào.")

    def display_borrowing_summary(self):
        """Hiển thị tổng hợp việc mượn sách."""
        for member_id, book_ids in self.borrowed_books.items():
            print(f"Thành viên {member_id} đã mượn:")
            for book_id in book_ids:
                if book_id in self.books:
                    self.books[book_id].display()
