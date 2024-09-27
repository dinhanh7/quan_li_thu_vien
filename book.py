class Book:
    def __init__(self, book_id, title, author, quantity=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity=quantity
    
    def display(self):
        print(f"ID: {self.book_id}\nTen sach: {self.title}\nTac gia: {self.author}\nCo san: {self.quantity}")

    def update_info(self):
        print("\nBan dang muon sua cuon sach sau:")
        self.display()
        sua1=input("Ban muon sua ID sach? (Yes/No)   ")
        if sua1=="Yes" or sua1=="yes":
            self.book_id = int(input("Hay nhap ID sach:"))
        sua2=input("Ban muon sua ten sach? (Yes/No)   ")
        if sua2=="Yes" or sua2=="yes":
            self.title = input("Hay nhap ten sach: ")
        sua3=input("Ban muon sua tac gia cua sach? (Yes/No)   ")
        if sua3=="Yes" or sua3=="yes":
            self.author = input("Hay nhap ten tac gia: ")
        sua4=input("Ban muon sua so luong sach co san? (Yes/No)   ")
        if sua4=="Yes" or sua4=="yes":
            self.quantity=int(input("So luong sach dang co san: "))
""" #doan nay dua vao module khac
    def borrow(self, soluong=1):
        if self.quantity-soluong<=0:
            print("Khong du sach nay de muon!")
        else:
            self.quantity=self.quantity-soluong
            print(f"\nSo sach {self.title} co san sau khi muon {soluong} cuon la: {self.quantity}")
    def back(self, soluong):
        self.quantity=self.quantity+soluong
        print(f"\nSo sach {self.title} co san sau khi tra {soluong} cuon la: {self.quantity}")
"""