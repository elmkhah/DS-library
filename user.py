from book import*
from linked_list import*
class user:
    def __init__(self,national_code=None,username=None,password=None,firstname=None,lastname=None,penalty=0,b_reserve1=None,b_reserve2=None,b_reserve3=None,b_reserve4=None,b_reserve5=None):
        self.username=username
        self.password=password
        self.firstname=firstname
        self.lastname=lastname
        self.national_code=national_code
        if username=='admin':
            self.is_admin=1
        else:
            self.is_admin=0

        if not penalty == 0:
            self.penalty=penalty
        else:
            self.penalty=0

        if b_reserve1==None:
            self.b_reserve1=None
        else:
            self.b_reserve1=b_reserve1

        if b_reserve2==None:
            self.b_reserve2=None
        else:
            self.b_reserve2=b_reserve2
        
        if b_reserve3==None:
            self.b_reserve3=None
        else:
            self.b_reserve3=b_reserve3
        
        if b_reserve4==None:
            self.b_reserve4=None
        else:
            self.b_reserve4=b_reserve4
        
        if b_reserve5==None:
            self.b_reserve5=None
        else:
            self.b_reserve5=b_reserve5

    ## login with username and password
    def login(user_list):
        #input data
        temp_user = user()
        temp_user.username=input("\nUsername: ")
        temp_user.password=input("Password: ")
        
        ## check username and password in linked list
        current_node = user_list.head
        while current_node:
            if current_node.data.username == temp_user.username:
                if current_node.data.password == temp_user.password:
                    print("log in successful")
                    return current_node.data               ##return current user
            current_node = current_node.next    
        print("Invalid username or password")     ##error
        return False
    
    def register(user_list):

        #input data
        temp_user=user()
        temp_user.firstname=input("firstname: ")
        temp_user.lastname=input("lastname: ")
        temp_user.national_code=int(input("national code: "))
        temp_user.username=input("username: ")
        temp_user.password=input("password: ")

        # check username and national code in linked list
        current_node = user_list.head
        while current_node:
            if current_node.data.username == temp_user.username or current_node.data.national_code == int(temp_user.national_code) :
                print("Duplicate user found")
                break
            current_node = current_node.next    
        user_list.insert_first(temp_user)
        print("user successfully created!")
        return temp_user   # return current user
    
    def add_book_to_user(self,_book):
        if self.b_reserve1==None:
            self.b_reserve1=_book
            return _book
        elif self.b_reserve2==None:
            self.b_reserve2=_book
            return _book
        elif self.b_reserve3==None:
            self.b_reserve3=_book
            return _book
        elif self.b_reserve4==None:
            self.b_reserve4=_book
            return _book
        elif self.b_reserve5==None:
            self.b_reserve5=_book
            return _book
        else:
            print("You booked the maximum possible number!")
            return
