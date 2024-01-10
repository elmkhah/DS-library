from _database import*
from datetime import datetime
from book import*
import os
import time

year=datetime.now().year
month=datetime.now().month
day=datetime.now().day
now=str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)
db=Database()
user_list = Database.get_users()
book_list = Database.get_books()
reserve_list=Database.get_reserves()


while(1):
    print("Welcome to DS-library\n1-login\n2-register\n0-exit")
    num=int(input())
    if(num==2):
        log=user.register(user_list)
        user_list.insert_first(log)
    elif(num==1):
        log=user.login(user_list)
    else:
        os.system('cls')
        print("Wishing you success, and goodbye!")
        break
    time.sleep(2)
    os.system('cls')
    if log:
        if int(log.is_admin):

            # admin futures:
            while(1):
                print("1-add a book\n2-reserve a book\n3-return a book\n4-extend a reserve\n0-back")
                num=int(input())
                if num==1:
                    book.add_book(book_list)
                elif num==2:
                    reserve.new_reserve_book(reserve_list,book_list,user_list)
                elif num==3:
                    print("return a book")
                elif num==4:
                    print("extend a reserve")
                elif num==0:
                    break
                Database.update_users(user_list)
                Database.update_books(book_list)
                Database.update_reserves(reserve_list)

            # normal user olny can see reserved books
        else:
            print("welcome,"+log.firstname+"!\nyour reservation:")
            counter=1
            if log.b_reserve1!='-':
                print(str(counter)+"- "+log.b_reserve1)
                counter+=1
            if log.b_reserve2!='-':
                print(str(counter)+"- "+log.b_reserve2)
                counter+=1
            if log.b_reserve3!='-':
                print(str(counter)+"- "+log.b_reserve3)
                counter+=1
            if log.b_reserve4!='-':
                print(str(counter)+"- "+log.b_reserve4)
                counter+=1
            if log.b_reserve5!='-':
                print(str(counter)+"- "+log.b_reserve5)
                counter+=1
            input("\n\npress <enter> to back to main menu:")
            
    os.system('cls')