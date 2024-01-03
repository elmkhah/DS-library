from book import*
class user:
    def __init__(self,national_code,username,password,firstname,lastname):
        self.username=username
        self.password=password
        self.firstname=firstname
        self.lastname=lastname
        self.national_code=national_code
        self.is_admin=False
        self.penalty=0
        self.b_reserve1="-"
        self.b_reserve2="-"
        self.b_reserve3="-"
        self.b_reserve4="-"
        self.b_reserve5="-"

        