from _database import*
from datetime import datetime
import os
import time

year=datetime.now().year
month=datetime.now().month
day=datetime.now().day
now=str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)

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

    