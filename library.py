from book import Book
from member import Member

class Library:
    # Tao doi tuong Library
    def __init__(self):
        self.books = {}  # Dictionary voi book_id la key va doi tuong Book la gia tri
        self.members = {}  # Dictionary voi member_id la key va doi tuong Member la gia tri
        self.borrowed_books = {}  # Dictionary voi member_id la key va danh sach book_id da muon

    # Them sach moi vao thu vien
    def add_book(self):
        while True:
            print("Nhap thong tin sach moi:")
            book_id = int(input("ID sach: "))
            title = input("Ten sach: ")
            author = input("Tac gia: ")
            quantity = int(input("So luong: "))

            # Kiem tra trung ID sach
            if book_id in self.books:
                existing_book = self.books[book_id]
                # Neu trung ca ID va ten sach, tang so luong sach
                if existing_book.title.lower() == title.lower():
                    existing_book.quantity += quantity
                    print(f"Da tang {quantity} cuon sach {title} (ID: {book_id}) trong thu vien.")
                else:
                    # Neu trung ID nhung ten sach khac, thong bao loi
                    print(f"ID {book_id} da duoc su dung cho sach {existing_book.title}. Vui long nhap ID khac.")
            else:
                # Kiem tra xem co sach nao trung ten nhung khac ID khong
                for book in self.books.values():
                    if book.title.lower() == title.lower():
                        print(f"Da ton tai sach co ten {title} voi ID {book.book_id}. Vui long nhap ten khac.")
                        break
                else:
                    # Neu khong co trung ID hoac ten, them sach moi
                    new_book = Book(book_id, title, author, quantity)
                    self.books[book_id] = new_book
                    print(f"Da them {quantity} cuon sach {title} (ID: {book_id}) vao thu vien.")
            
            tiep_tuc = input("Ban co muon tiep tuc them sach? (Yes/No): ").strip().lower()
            if tiep_tuc == 'no':
                break




    # Xoa sach khoi thu vien
    def remove_book(self):
        while True:
            choice = input("Ban muon xoa sach bang ID hay ten? (Nhap 'ID' hoac 'ten'): ").strip().lower()

            if choice == 'id':
                book_id = int(input("Nhap ID sach: "))
                if book_id in self.books:
                    del self.books[book_id]
                    print("Sach da bi xoa khoi he thong.")
                else:
                    print("Khong tim thay sach voi ID nay.")
            
            elif choice == 'ten':
                title = input("Nhap ten sach: ").strip()
                found = False
                for book_id, book in list(self.books.items()):
                    if book.title.lower() == title.lower():
                        del self.books[book_id]
                        found = True
                        print(f"Sach {title} da bi xoa khoi he thong.")
                        break
                if not found:
                    print(f"Khong tim thay sach voi ten {title}.")
            
            else:
                print("Lua chon khong hop le.")

            tiep_tuc = input("Ban co muon tiep tuc xoa sach? (Yes/No): ").strip().lower()
            if tiep_tuc == 'no':
                break



    # Cap nhat thong tin sach
    def update_book(self):
        choice = input("Ban muon sua sach bang ID hay ten? (Nhap 'ID' hoac 'ten'): ").strip().lower()

        if choice == 'id':
            book_id = int(input("Nhap ID sach: "))
            if book_id in self.books:
                book = self.books[book_id]
            else:
                print("Khong tim thay sach voi ID nay.")
                return

        elif choice == 'ten':
            title = input("Nhap ten sach: ").strip()
            book = None
            for b in self.books.values():
                if b.title.lower() == title.lower():
                    book = b
                    break
            if not book:
                print(f"Khong tim thay sach voi ten {title}.")
                return

        else:
            print("Lua chon khong hop le.")
            return

        print("Thong tin hien tai cua sach:")
        book.display()

        while True:
            sua_id = input("Ban co muon sua ID sach? (Yes/No): ").strip().lower()
            if sua_id == 'yes':
                book.book_id = int(input("Nhap ID sach moi: "))

            sua_title = input("Ban co muon sua ten sach? (Yes/No): ").strip().lower()
            if sua_title == 'yes':
                book.title = input("Nhap ten sach moi: ")

            sua_author = input("Ban co muon sua tac gia? (Yes/No): ").strip().lower()
            if sua_author == 'yes':
                book.author = input("Nhap tac gia moi: ")

            sua_quantity = input("Ban co muon sua so luong? (Yes/No): ").strip().lower()
            if sua_quantity == 'yes':
                book.quantity = int(input("Nhap so luong moi: "))

            tiep_tuc = input("Ban co muon tiep tuc sua sach khac? (Yes/No): ").strip().lower()
            if tiep_tuc == 'no':
                break


    # Them thanh vien moi vao he thong thu vien
    def add_member(self):
        while True:
            print("Nhap thong tin thanh vien moi:")
            member_id = input("MSSV: ")
            name = input("Ten thanh vien: ")
            phone = input("So dien thoai: ")

            if member_id in self.members or name in self.members:
                print("Thanh vien da ton tai.")
            else:
                new_member = Member(member_id, name, phone)
                self.members[member_id] = new_member
                self.borrowed_books[member_id] = []
                print(f"Da them thanh vien {name} vao he thong.")
            
            tiep_tuc = input("Ban co muon tiep tuc them thanh vien? (Yes/No): ").strip().lower()
            if tiep_tuc == 'no':
                break
    # Sua thong tin thanh vien
    def update_member(self):
        choice = input("Ban muon sua thanh vien bang MSSV hay ten? (Nhap 'MSSV' hoac 'ten'): ").strip().lower()

        if choice == 'mssv':
            member_id = input("Nhap MSSV thanh vien: ").strip()
            if member_id in self.members:
                member = self.members[member_id]
            else:
                print("Khong tim thay thanh vien voi MSSV nay.")
                return

        elif choice == 'ten':
            name = input("Nhap ten thanh vien: ").strip()
            member = None
            for m in self.members.values():
                if m.name.lower() == name.lower():
                    member = m
                    break
            if not member:
                print(f"Khong tim thay thanh vien voi ten {name}.")
                return

        else:
            print("Lua chon khong hop le.")
            return

        print("Thong tin hien tai cua thanh vien:")
        member.display()

        while True:
            sua_mssv = input("Ban co muon sua MSSV? (Yes/No): ").strip().lower()
            if sua_mssv == 'yes':
                member.member_id = input("Nhap MSSV moi: ")

            sua_name = input("Ban co muon sua ten? (Yes/No): ").strip().lower()
            if sua_name == 'yes':
                member.name = input("Nhap ten moi: ")

            sua_phone = input("Ban co muon sua so dien thoai? (Yes/No): ").strip().lower()
            if sua_phone == 'yes':
                member.phone_number = input("Nhap so dien thoai moi: ")

            tiep_tuc = input("Ban co muon tiep tuc sua thanh vien khac? (Yes/No): ").strip().lower()
            if tiep_tuc == 'no':
                break


    # Xoa thanh vien khoi he thong
    def remove_member(self):
        while True:
            choice = input("Ban muon xoa thanh vien bang MSSV hay ten? (Nhap 'MSSV' hoac 'ten'): ").strip().lower()

            if choice == 'mssv':
                member_id = input("Nhap MSSV thanh vien: ").strip()
                if member_id in self.members:
                    del self.members[member_id]
                    del self.borrowed_books[member_id]
                    print("Thanh vien da bi xoa khoi he thong.")
                else:
                    print("Khong tim thay thanh vien voi MSSV nay.")
            
            elif choice == 'ten':
                name = input("Nhap ten thanh vien: ").strip()
                found = False
                for member_id, member in list(self.members.items()):
                    if member.name.lower() == name.lower():
                        del self.members[member_id]
                        del self.borrowed_books[member_id]
                        found = True
                        print(f"Thanh vien {name} da bi xoa khoi he thong.")
                        break
                if not found:
                    print(f"Khong tim thay thanh vien voi ten {name}.")
            
            else:
                print("Lua chon khong hop le.")

            tiep_tuc = input("Ban co muon tiep tuc xoa thanh vien? (Yes/No): ").strip().lower()
            if tiep_tuc == 'no':
                break


    # Muon sach
    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Thanh vien khong ton tai.")
            return
        if book_id not in self.books:
            print("Sach khong ton tai.")
            return
        if self.books[book_id].quantity <= 0:
            print("Sach da het.")
            return
        self.books[book_id].quantity -= 1
        self.borrowed_books[member_id].append(book_id)
        print(f"Thanh vien {self.members[member_id].name} da muon sach {self.books[book_id].title}.")

    # Tra sach
    def return_book(self, member_id, book_id):
        if member_id not in self.borrowed_books or book_id not in self.borrowed_books[member_id]:
            print("Khong tim thay sach dang muon.")
            return
        self.borrowed_books[member_id].remove(book_id)
        self.books[book_id].quantity += 1
        print(f"Thanh vien {self.members[member_id].name} da tra sach {self.books[book_id].title}.")

    # Hien thi tat ca sach trong thu vien
    def display_books(self):
        if not self.books:
            print("Khong co sach trong thu vien.")
        else:
            print("\nDanh sach cac sach trong thu vien:")
            for book in self.books.values():
                book.display()

    # Hien thi tat ca thanh vien
    def display_members(self):
        if not self.members:
            print("Khong co thanh vien trong he thong.")
        else:
            print("\nDanh sach cac thanh vien:")
            for member in self.members.values():
                member.display()

    # Hien thi thong tin sach dang muon cua thanh vien
    def display_member_borrowing(self, member_id):
        if member_id not in self.members:
            print("Thanh vien khong ton tai.")
            return
        member = self.members[member_id]
        print(f"\nThong tin thanh vien:")
        member.display()
        print(f"Thanh vien {member.name} dang muon cac sach sau:")
        if not self.borrowed_books[member_id]:
            print("Khong muon sach nao.")
        else:
            for book_id in self.borrowed_books[member_id]:
                self.books[book_id].display()
    
    # Hien thi danh sach thanh vien va so sach ho muon
    def display_borrowing_summary(self):
        if not self.borrowed_books:
            print("Khong co sach dang duoc muon.")
        else:
            print("\nDanh sach cac thanh vien va so luong sach ho muon:")
            for member_id, borrowed in self.borrowed_books.items():
                print(f"Thanh vien: {self.members[member_id].name} - So sach dang muon: {len(borrowed)}")
