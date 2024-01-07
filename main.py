from _database import*
import os
import time
user_list = Database.get_users()
book_list = Database.get_books()
# reserve_list=Database.get_reserves()


while(1):
    print("Welcome to DS-library\n1-login\n2-register\n0-exit")
    num=int(input())
    if(num==2):
        log=user.register(user_list)
    elif(num==1):
        log=user.login(user_list)
    elif(num==0):
        os.system('cls')
        print("Wishing you success, and goodbye!")
        break
    time.sleep(2)
    os.system('cls')