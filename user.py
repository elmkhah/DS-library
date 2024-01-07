from book import*
from linked_list import*
class user:
    def __init__(self,national_code=None,username=None,password=None,firstname=None,lastname=None):
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
                    return temp_user               ##return current user
            current_node = current_node.next    
        print("Invalid username or password")     ##error
        return False
    
    def register(user_list):

        #input data
        temp_user=user()
        temp_user.firstname=input("firstname: ")
        temp_user.lastname=input("lastname: ")
        temp_user.national_code=input("national code: ")
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
        return temp_user   # return current user