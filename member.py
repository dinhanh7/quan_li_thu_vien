class Member:
    def __init__(self, mssv, name, phone):
        self.member_id = mssv
        self.name = name
        self.phone_number = phone

    def display(self):
        print(f"MSSV: {self.mssv}, Name: {self.name}, Phone number: {self.phone}")

    def update_info(self,mssv, name, phone):
        print("\nBan dang muon sua thong tin nguoi sau:")
        self.display()
        sua1=input("Ban muon sua MSSV? (Yes/No)   ")
        if sua1=="Yes" or sua1=="yes":
            self.book_id = int(input("Hay nhap MSSV: "))
        sua2=input("Ban muon sua ten? (Yes/No)   ")
        if sua2=="Yes" or sua2=="yes":
            self.book_id = input("Hay nhap ten: ")
        sua3=input("Ban muon sua so dien thoai? (Yes/No)   ")
        if sua3=="Yes" or sua3=="yes":
            self.book_id = int(input("Hay nhap so dien thoai: "))