from user import*
from book import*
from datetime import datetime
year=datetime.now().year
month=datetime.now().month
day=datetime.now().day
now=str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)


class reserve:
    def __init__(self,applicant=None,r_book=None,start_reserve_date=None,start_waiting_date=None,start_date=None,end_date=None,is_received=False,is_returned=False):
        self.ID=-1
        self.applicant=applicant
        self.r_book=r_book
        self.start_reserve_date=start_reserve_date
        self.start_waiting_date=start_waiting_date
        self.start_date=start_date
        self.end_date=end_date
        self.is_received=is_received
        self.is_returned=is_returned

    def new_reserve_book(reserve_list,book_list,user_list):
        temp_reserves=reserve()
        temp_reserves.applicant=input("Applicant username: ")
        temp_reserves.r_book=input("book title: ")
        temp_reserves.start_reserve_date=now

        #exception
        exist=0
        current_node=book_list.head
        while current_node:
            if current_node.data.title==temp_reserves.r_book:
                exist=1
            current_node=current_node.next
        if exist==0:
            print("book not found!")
            return
        
        exist=0
        current_node=user_list.head
        while current_node:
            if current_node.data.username==temp_reserves.applicant:
                exist=1
            current_node=current_node.next
        if exist==0:
             print("user not found!")
             return
        
        reserve_list.append(temp_reserves)
        return 1