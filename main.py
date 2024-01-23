from _database import*
from datetime import datetime
from book import*
from reserve_queue import*
from reserve import*
import os
import time
year=datetime.now().year
month=datetime.now().month
day=datetime.now().day
now=str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)

# Database.delete()
user_list = Database.get_users()
book_list = Database.get_books()
reserve_list=Database.get_reserves()
reserve_queue=reserve.create_reserve_queue(reserve_list,book_list)
reserve.check_waiting_date(reserve_list)

while(1):
    print("Welcome to DS-library\n1-login\n2-register\n0-exit")
    num=input()
    if(num=='2'):
        log=user.register(user_list)
        user_list.insert_first(log)
    elif(num=='1'):
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
                print("\n1-add a book\n2-reserve a book\n3-return a book\n4-extend a reserve\n5-get reserved book\n0-back")
                num=input()
                if num=='1':
                    book.add_book(book_list)
                elif num=='2':
                    reserve.new_reserve_book(reserve_list,book_list,user_list,reserve_queue)
                elif num=='3':
                    reserve.return_book(book_list,reserve_list,user_list,reserve_queue)
                elif num=='4':
                    reserve.expand_reserve(book_list,reserve_list,reserve_queue)
                elif num=='5':
                    reserve.get_reserved_book(user_list,book_list,reserve_list,reserve_queue)
                else:
                    break
                Database.update_users(user_list)
                Database.update_books(book_list)
                Database.update_reserves(reserve_list)
                book_list=Database.get_books()
                user_list=Database.get_users()
                reserve_list=Database.get_reserves()
                reserve.create_reserve_queue(reserve_list,book_list)

            # normal user olny can see reserved books
        else:
            print("welcome,"+log.firstname+"!\nyour reservation:")
            counter=1
            if log.b_reserve1:
                print(counter,end=" ")
                print("- "+log.b_reserve1)
                counter+=1
            if log.b_reserve2:
                print(counter,end=" ")
                print("- "+log.b_reserve2)
                counter+=1
            if log.b_reserve3:
                print(counter,end=" ")
                print("- "+log.b_reserve3)
                counter+=1
            if log.b_reserve4:
                print(counter,end=" ")
                print("- "+log.b_reserve4)
                counter+=1
            if log.b_reserve5:
                print(counter,end=" ")
                print("- "+log.b_reserve5)
                counter+=1
            input("\n\npress <enter> to back to main menu:")
            
    os.system('cls')