from user import*
from book import*
from reserve_queue import _Queue
from datetime import datetime,timedelta
_end_time=datetime.now()+timedelta(days=10)
_end=str(_end_time.year).zfill(4)+str(_end_time.month).zfill(2)+str(_end_time.day).zfill(2)
year=datetime.now().year
month=datetime.now().month
day=datetime.now().day
now=str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)


class reserve:
    def __init__(self,ID=-1,applicant=None,r_book=None,start_reserve_date=None,start_waiting_date=None,start_date=None,end_date=None,is_received=False,is_returned=False):
        self.ID=ID
        self.applicant=applicant
        self.r_book=r_book
        self.start_reserve_date=start_reserve_date
        self.start_waiting_date=start_waiting_date
        self.start_date=start_date
        self.end_date=end_date
        self.is_received=is_received
        self.is_returned=is_returned

    def new_reserve_book(reserve_list,book_list,user_list,reserve_queue):
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
                book_ID=current_node.data.ID-1
                break
            current_node=current_node.next
        if exist==0:
            print("book not found!")
            return
        
        exist=0
        current_node=user_list.head
        while current_node:
            if current_node.data.username==temp_reserves.applicant:
                exist=1
                temp_user=current_node.data
                break
            current_node=current_node.next
        if exist==0:
             print("user not found!")
             return
        
        if temp_reserves.r_book==temp_user.b_reserve1 or temp_reserves.r_book==temp_user.b_reserve2 or temp_reserves.r_book==temp_user.b_reserve3 or temp_reserves.r_book==temp_user.b_reserve4 or temp_reserves.r_book==temp_user.b_reserve5:
            print("you are already reserved this book!")
            return

        if reserve_queue[book_ID].first() and reserve_queue[book_ID].first().applicant!=temp_reserves.applicant:
            print("you are added to reserve queue!")
            reserve_list.append(temp_reserves)
            return
        

        reserve_queue[book_ID].enqueue(temp_reserves)
        if temp_user.b_reserve1==None and temp_user.b_reserve1!=temp_reserves.r_book:
            temp_user.b_reserve1=temp_reserves.r_book
        elif temp_user.b_reserve2==None and temp_user.b_reserve2!=temp_reserves.r_book:
            temp_user.b_reserve2=temp_reserves.r_book
        elif temp_user.b_reserve3==None and temp_user.b_reserve3!=temp_reserves.r_book:
            temp_user.b_reserve3=temp_reserves.r_book
        elif temp_user.b_reserve4==None and temp_user.b_reserve4!=temp_reserves.r_book:
            temp_user.b_reserve4=temp_reserves.r_book
        elif temp_user.b_reserve5==None and temp_user.b_reserve5!=temp_reserves.r_book:
            temp_user.b_reserve5=temp_reserves.r_book  
        else:
            print("You booked the maximum possible number")
            return  
        
        temp_reserves.is_received=1
        temp_reserves.start_waiting_date=now
        temp_reserves.start_date=now
        temp_reserves.end_date=_end
        reserve_list.append(temp_reserves)
        print("book reserved successfully!")
        return 1
    
    def create_reserve_queue(reserve_list,book_list):
        reserve_queue=[]
        current_node=book_list.head
        while current_node:
            queue_list=_Queue()
            if reserve_list:
                for i in reserve_list:
                    if i.r_book==current_node.data.title and not i.is_returned:
                        queue_list.enqueue(i)
            reserve_queue.append(queue_list)
            current_node=current_node.next
        return reserve_queue