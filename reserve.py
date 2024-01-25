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


    #reserve new book
    def new_reserve_book(reserve_list,book_list,user_list,reserve_queue):
        
        #input data
        temp_reserves=reserve()
        temp_reserves.applicant=input("Applicant username: ")
        temp_reserves.r_book=input("book title: ")
        temp_reserves.start_reserve_date=now

        #search in books with AVL
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
        
        #search in users
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
        
        #search in reserves to found duplicate reserve
        for i in reserve_list:
            if i.applicant==temp_reserves.applicant and i.r_book==temp_reserves.r_book and i.is_received==0:
                print("you are already reserved this book!")
                return
        
        #when book already reserved by you
        if temp_reserves.r_book==temp_user.b_reserve1 or temp_reserves.r_book==temp_user.b_reserve2 or temp_reserves.r_book==temp_user.b_reserve3 or temp_reserves.r_book==temp_user.b_reserve4 or temp_reserves.r_book==temp_user.b_reserve5:
            print("you are already reserved this book!")
            return

        #when book is reserved - and you add to reserve queue
        if reserve_queue[book_ID].first() and reserve_queue[book_ID].first().applicant!=temp_reserves.applicant:
            print("you are added to reserve queue!")
            reserve_list.append(temp_reserves)
            return
        

        #find a empity resreve capacity
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
        

        #final set for receive book
        temp_reserves.is_received=1
        temp_reserves.start_waiting_date=now
        temp_reserves.start_date=now
        temp_reserves.end_date=_end
        reserve_list.append(temp_reserves)
        print("book reserved successfully!")
        return 1
    
    #create a array in number of books. that which array cell include resserve queue of this book
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
    
    #check if now - waiting_date >3 and book is not received; reservation is cancel
    #start waiting date to first person in queue
    def check_waiting_date(reserve_list,reserve_queue):
        #check waiting_date
        for i in reserve_list:
            if i.start_waiting_date and not i.is_received:
                wait_date=str(i.start_waiting_date)
                waiting=datetime(year=int(wait_date[0:4]), month=int(wait_date[4:6]), day=int(wait_date[6:8]))
                return_time=datetime.now()-waiting
                if return_time.days>3:
                    i.is_received=1
                    i.is_returned=1

        #start waiting_date to first person in queue
        for i in reserve_queue:
            if i.first() and not i.first().start_waiting_date:
                i.first().start_waiting_date=now
                for j in reserve_list:
                    if j.applicant==i.first().applicant and j.r_book==i.first().r_book:
                        j.start_waiting_date=now
        return reserve_list,reserve_queue
    
    #receive the book that ready to be taken - if you are added in reserve queue
    def get_reserved_book(user_list,book_list,reserve_list,reserve_queue):
        temp_reserve=reserve()
        temp_reserve.applicant=input("Applicant username: ")
        temp_reserve.r_book=input("book title: ")
        
        #search books in AVL tree
        book_ID=-1
        book_avl=AVLTree()
        current_node=book_list.head
        while current_node:
            book_avl.insert_key(current_node.data)
            current_node=current_node.next
        if book_avl.search(temp_reserve.r_book):
            book_search=book_avl.search(temp_reserve.r_book)
            book_ID=book_search.key.ID-1
        
         
        #serach user
        current_node=user_list.head
        while current_node:
            if current_node.data.username==temp_reserve.applicant:
                temp_user=current_node.data
                break
            current_node=current_node.next

        #search reserve
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
        
        #final set to receive book
        temp_reserve.is_received=1
        temp_reserve.start_date=now
        temp_reserve.end_date=_end
        reserve_list[temp_reserve.ID-1]=temp_reserve

        result=temp_user.add_book_to_user(temp_reserve.r_book)
        if not result:
            return
        
        print("the book was successfully delivered!")

        return reserve_list

    #expand (tamdid) reserve
    def expand_reserve(book_list,reserve_list,reserve_queue):
        temp_reserve=reserve()
        temp_reserve.applicant=input("applicant username: ")
        temp_reserve.r_book=input("book title: ")

        #search book in AVL tree
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

        
        #search in reserves
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


    #return the book that received - and show & save penalty
    def return_book(book_list,reserve_list,user_list,reserve_queue):
        temp_reserve=reserve()
        temp_reserve.applicant=input("applicant username: ")
        temp_reserve.r_book=input("book title: ")
        
        #search book in AVL tree
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
        exist=0

        #search in users
        current_node=user_list.head
        while current_node:
            if current_node.data.username==temp_reserve.applicant:
                exist=1
                temp_user=current_node.data
                break
            current_node=current_node.next
        if exist==0:
             print("user not found!")
             return
        
        #search in reserves
        for i in reserve_list:
            if i.applicant==temp_reserve.applicant and i.r_book==temp_reserve.r_book and not i.is_returned:
                i.is_returned=1
                date_end=str(i.end_date)
                if not i.end_date:
                    print("reserve not found!")
                    return
                date=datetime(year=int(date_end[0:4]), month=int(date_end[4:6]), day=int(date_end[6:8]))
                return_time=datetime.now()-date
                if return_time.days>0:
                    temp_user.penalty+=return_time.days    #penalty
                    print("your total penalty: "+str(temp_user.penalty))

                    #start waiting date to first person in queue
                    if reserve_queue[book_ID].secend():
                        reserve_queue[book_ID].secend().waiting_date=now
                        for j in reserve_list:
                            if j.applicant==reserve_queue[book_ID].secend().applicant and j.r_book==reserve_queue[book_ID].secend().r_book:
                                j.start_waiting_date=now
        
        #clear book from user's books
        if not temp_user.b_reserve1==None and temp_user.b_reserve1==book_search.key.title:
            temp_user.b_reserve1=None
        elif not temp_user.b_reserve2==None and temp_user.b_reserve2==book_search.key.title:
            temp_user.b_reserve2=None
        elif not temp_user.b_reserve3==None and temp_user.b_reserve3==book_search.key.title:
            temp_user.b_reserve3=None
        elif not temp_user.b_reserve4==None and temp_user.b_reserve4==book_search.key.title:
            temp_user.b_reserve4=None
        elif not temp_user.b_reserve5==None and temp_user.b_reserve5==book_search.key.title:
            temp_user.b_reserve5=None
        print("book returned successfully!!")