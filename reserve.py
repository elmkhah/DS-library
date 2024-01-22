from user import*
from book import*
from AVL import*
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
        
        
        book_avl=AVLTree()
        
        current_node=book_list.head
        while current_node:
            book_avl.insert_key(current_node.data)
            current_node=current_node.next
        if book_avl.search(temp_reserves.r_book) is None:
            exist=0
        else:
            book_search=book_avl.search(temp_reserves.r_book)
            book_ID=book_search.key.ID-1
            exist=1 
       
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
        
        for i in reserve_list:
            if i.applicant==temp_reserves.applicant and i.r_book==temp_reserves.r_book and i.is_received==0:
                print("you are already reserved this book!")
                return
        
        if temp_reserves.r_book==temp_user.b_reserve1 or temp_reserves.r_book==temp_user.b_reserve2 or temp_reserves.r_book==temp_user.b_reserve3 or temp_reserves.r_book==temp_user.b_reserve4 or temp_reserves.r_book==temp_user.b_reserve5:
            print("you are already reserved this book!")
            return

        if reserve_queue[book_ID].first() and reserve_queue[book_ID].first().applicant!=temp_reserves.applicant:
            print("you are added to reserve queue!")
            reserve_list.append(temp_reserves)
            return
        

        reserve_queue[book_ID].enqueue(temp_reserves)
        if temp_user.b_reserve1==None:
            temp_user.b_reserve1=temp_reserves.r_book
        elif temp_user.b_reserve2==None:
            temp_user.b_reserve2=temp_reserves.r_book
        elif temp_user.b_reserve3==None:
            temp_user.b_reserve3=temp_reserves.r_book
        elif temp_user.b_reserve4==None:
            temp_user.b_reserve4=temp_reserves.r_book
        elif temp_user.b_reserve5==None:
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
            reserve_queue.insert(0,queue_list)
            current_node=current_node.next
        return reserve_queue
    
    def check_waiting_date(reserve_list):
        for i in reserve_list:
            if i.start_waiting_date and not i.is_received:
                waiting=datetime(i.start_waiting_date[0:4],i.start_waiting_date[4:6],i.start_waiting_date[6:8])
                receive_time=now-waiting
                receive_time=receive_time.days
                if(receive_time>3):
                    i.is_received=True
                    i.is_returned=True
    def get_reserved_book(user_list,book_list,reserve_list,reserve_queue):
        temp_reserve=reserve()
        temp_reserve.applicant=input("Applicant username: ")
        temp_reserve.r_book=input("book title: ")
        book_ID=-1
        book_avl=AVLTree()
        
        current_node=book_list.head
        while current_node:
            book_avl.insert_key(current_node.data)
            current_node=current_node.next
        if book_avl.search(temp_reserve.r_book):
            book_search=book_avl.search(temp_reserve.r_book)
            book_ID=book_search.key.ID-1
        
         

        current_node=user_list.head
        while current_node:
            if current_node.data.username==temp_reserve.applicant:
                temp_user=current_node.data
                break
            current_node=current_node.next

        is_found=False
        for i in reserve_list:
            if temp_reserve.applicant == i.applicant and temp_reserve.r_book==i.r_book and not i.is_received:
                is_found=True
                temp_reserve=i
                if reserve_queue[book_ID-1].first() and reserve_queue[book_ID-1].first().applicant != i.applicant:
                    print("The book has not returned yet!")
                    return
                
        if not is_found:
            print("reserve not found!")
            return
        
        temp_reserve.is_received=1
        temp_reserve.start_date=now
        temp_reserve.end_date=_end
        reserve_list[temp_reserve.ID-1]=temp_reserve

        result=temp_user.add_book_to_user(temp_reserve.r_book)
        if not result:
            return
        
        print("the book was successfully delivered!")

        return reserve_list

    def expand_reserve(book_list,reserve_list,reserve_queue):
        temp_reserve=reserve()
        temp_reserve.applicant=input("applicant username: ")
        temp_reserve.r_book=input("book title: ")

        book_ID=-1
        book_avl=AVLTree()
        
        current_node=book_list.head
        while current_node:
            book_avl.insert_key(current_node.data)
            current_node=current_node.next
        if book_avl.search(temp_reserve.r_book):
            book_search=book_avl.search(temp_reserve.r_book)
            book_ID=book_search.key.ID-1
        else:
            print("reserve not found!")
            return

        for i in reserve_list:
            if i.applicant==temp_reserve.applicant and i.r_book==temp_reserve.r_book and not i.is_returned:
                if reserve_queue[book_ID].first() and reserve_queue[book_ID].first().applicant==temp_reserve.applicant:
                    i.end_date=_end
                    print("The book was extended for 10 days!")
                    return 1
                print("Unsuccessful! Other people are waiting for this book!")
                return
        print("reserve not found!")
        return


    def return_book():
        print(30)