import sqlite3
from user import*
from book import*
from reserve import*
from linked_list import*

##  database configuration
con=sqlite3.connect("library.db")
cur=con.cursor()

class Database:

    # create tables
    def __init__(self):
        cur.execute("CREATE TABLE IF NOT EXISTS users(national_code PRIMARY KEY,firstname VARCHAR(50),lastname VARCHAR(50),username VARCHAR(100),password VARCHAR(100),penalty INT,is_admin BOOLEAN, b_reserve1 VARCHAR(100),b_reserve2 VARCHAR(100),b_reserve3 VARCHAR(100),b_reserve4 VARCHAR(100),b_reserve5 VARCHAR(100))")   
        con.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS books(ID INTEGER PRIMARY KEY,title VARCHAR(100),content VARCHAR(50),publication_year VARCHAR(4),writer VARCHAR(50))")
        con.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS reserves(ID INTEGER PRIMARY KEY,applicant INT(10),r_book VARCHAR(100),start_reserve_date INT(8),start_waiting_date INT(8),start_date INT(8),end_date INT(8),is_received BOOLEAN,is_returned BOOLEAN)")
        con.commit()
        
    # read users from database and add to linked list
    def get_users():
        _users=LinkedList()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        for i in users:
            _user=user(national_code=i[0],username=i[3],password=i[4],firstname=i[1],lastname=i[2],penalty=i[5],b_reserve1=i[7],b_reserve2=i[8],b_reserve3=i[9],b_reserve4=i[10],b_reserve5=i[11])
            _users.insert_first(_user)
        return _users
    
    # read reserves from database and add to array
    def get_reserves():
        _reserves= []
        cur.execute("SELECT * FROM reserves")
        reserves=cur.fetchall()
        for i in reserves:
            _reserve=reserve(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            _reserves.append(_reserve)
        return _reserves 

    #read books from database and add to linked list
    def get_books():
        _books=LinkedList()
        cur.execute("SELECT * FROM books")
        books=cur.fetchall()
        for i in books:
            _book=book(i[0],i[1],i[2],i[3],i[4])
            _books.insert_first(_book)
        return _books
    
    #write new updated users into database(from linked list)
    def update_users(_users):
        user=_users.head
        while user:
            cur.execute("SELECT * FROM users WHERE national_code=?", (user.data.national_code,))
            existing_user = cur.fetchone()

            if existing_user:
                cur.execute("UPDATE users SET b_reserve1=? ,b_reserve2=? ,b_reserve3=? ,b_reserve4=? ,b_reserve5=? ,penalty=? WHERE national_code=?", (user.data.b_reserve1,user.data.b_reserve2,user.data.b_reserve3,user.data.b_reserve4,user.data.b_reserve5,user.data.penalty,user.data.national_code))
            else:
                cur.execute("INSERT INTO users (national_code, firstname, lastname, username, password, penalty, b_reserve1, b_reserve2, b_reserve3, b_reserve4, b_reserve5, is_admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user.data.national_code, user.data.firstname, user.data.lastname, user.data.username, user.data.password, user.data.penalty, user.data.b_reserve1, user.data.b_reserve2, user.data.b_reserve3, user.data.b_reserve4, user.data.b_reserve5, user.data.is_admin))
            con.commit()
            user=user.next

    #write new updated books into database(from linked list)
    def update_books(_books):
        book=_books.head
        while book:
            cur.execute("SELECT * FROM books WHERE title=?", (book.data.title,))
            existing_book = cur.fetchone()

            if existing_book:
                book=book.next
                continue
            else:
                cur.execute("INSERT INTO books (title, content, publication_year,writer) VALUES (?, ?, ?, ?)",(book.data.title,book.data.content,book.data.publication_year,book.data.writer))
            con.commit()
            book=book.next

    #write new updated reserves into database(from array)
    def update_reserves(_reserves):
        for reserve in _reserves:
            cur.execute("SELECT * FROM reserves WHERE ID=?", (reserve.ID,))
            existing_reserve = cur.fetchone()

            if existing_reserve:
                cur.execute("UPDATE reserves SET start_waiting_date=? ,start_date=? ,end_date=? ,is_received=? ,is_returned=? WHERE ID=?", (reserve.start_waiting_date,reserve.start_date,reserve.end_date,reserve.is_received,reserve.is_returned,reserve.ID))
            else:
                cur.execute("INSERT INTO reserves (applicant, r_book, start_reserve_date, start_waiting_date, start_date, end_date, is_received, is_returned) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(reserve.applicant,reserve.r_book,reserve.start_reserve_date,reserve.start_waiting_date,reserve.start_date,reserve.end_date,reserve.is_received,reserve.is_returned))
            con.commit()

    #read last ID in books and reserves : enter at type: "books" or "reserves"
    # def last_ID(type):
    #     if(type=="books"):
    #         index=cur.execute("SELECT MAX(ID) FROM books")
    #         return index
    #     elif(type=="reserves"):
    #         index=cur.execute("SELECT MAX(ID) FROM reserves")
    #         return index
    #     else:
    #         return -1
            
    def delete():
        cur.execute("DELETE FROM reserves WHERE ID>0")
        con.commit()