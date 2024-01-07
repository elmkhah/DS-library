import sqlite3
from datetime import datetime
from user import*
from book import*
from reserve import*
from linked_list import*

year=datetime.now().year
month=datetime.now().month
day=datetime.now().day
now=str(year).zfill(4)+str(month).zfill(2)+str(day).zfill(2)
con=sqlite3.connect("library.db")
cur=con.cursor()

class Database:
    def __init__():
        cur.execute("CREATE TABLE IF NOT EXISTS users(national_code INT(10) PRIMARY KEY,firstname VARCHAR(50),lastname VARCHAR(50),username VARCHAR(100),password VARCHAR(100),penalty INT,is_admin BOOLEAN, b_reserve1 VARCHAR(100),b_reserve2 VARCHAR(100),b_reserve3 VARCHAR(100),b_reserve4 VARCHAR(100),b_reserve5 VARCHAR(100))")   
        con.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS books(ID INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(100),content VARCHAR(50),publication_year VARCHAR(4),writer VARCHAR(50))")
        con.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS reserves(ID INT AUTO_INCREMENT PRIMARY KEY,applicant INT(10),r_book VARCHAR(100),start_reserve_date INT(8),start_waiting_date INT(8),start_date INT(8),end_date INT(8),is_received BOOLEAN,is_returned BOOLEAN)")
        con.commit()
        
    def get_users():
        _users=LinkedList()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        for i in users:
            _user=user(i[0],i[3],i[4],i[1],i[2])
            _users.insert_first(_user)
        return _users
    
    # def get_reserves():
    #     _reserves=LinkedList()
    #     cur.execute("SELECT * FROM reserves")
    #     reserves=cur.fetchall()
    #     for i in reserves:
    #         _reserve=reserve()
    #     return _reserves 
    def get_books():
        cur.execute("SELECT * FROM books")
        books=cur.fetchall()
        return books
    def get_all():
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        cur.execute("SELECT * FROM reserves")
        reserves=cur.fetchall()
        cur.execute("SELECT * FROM books")
        books=cur.fetchall()
        return users,books,reserves

    def update_users(self,_users):
        for user in _users:
            cur.execute("SELECT * FROM users WHERE national_code=?", (user.national_code,))
            existing_user = cur.fetchone()

            if existing_user:
                cur.execute("UPDATE users SET b_reserve1=? ,b_reserve2=? ,b_reserve3=? ,b_reserve4=? ,b_reserve5=? ,penalty=?, WHERE national_code=?", (user.b_reserve1,user.b_reserve2,user.b_reserve3,user.b_reserve4,user.b_reserve5,user.penalty, user.national_code))
            else:
                cur.execute("INSERT INTO users (national_code, firstname, lastname, username, password,penalty,b_reserve1,b_reserve2,b_reserve3,b_reserve4,b_reserve5,is_admin,) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)",(user.national_code, user.firstname, user.lastname, user.username, user.password,user.penalty,user.b_reserve1,user.b_reserve2,user.b_reserve3,user.b_reserve4,user.b_reserve5,user.is_admin))
            con.commit()
    def update_books(self,_books):
        for book in _books:
            cur.execute("SELECT * FROM books WHERE ID=?", (book.ID,))
            existing_book = cur.fetchone()

            if existing_book:
                continue
            else:
                cur.execute("INSERT INTO books (title, content, publication_year,wrtier,) VALUES (?, ?, ?, ?, ?)",(book.title,book.content,book.publication_year,book.writer))
            con.commit()
    def update_reserves(self,_reserves):
        for reserve in _reserves:
            cur.execute("SELECT * FROM reserves WHERE ID=?", (reserve.ID,))
            existing_reserve = cur.fetchone()

            if existing_reserve:
                cur.execute("UPDATE reserves SET start_waiting_date=? ,start_date=? ,end_date=? ,is_received=? ,is_returned=?", (reserve.start_waiting_date,reserve.start_date,reserve.end_date,reserve.is_received,reserve.is_returned))
            else:
                cur.execute("INSERT INTO reserves (applicant, r_book, start_reserve_date, start_waiting_date, start_date, end_date, is_received, is_returned,) VALUES (?, ?, ?, ?, ?, ?, ?, ?,)",(reserve.applicant,reserve.r_book,reserve.start_reserve_date,reserve.start_waiting_date,reserve.start_date,reserve.end_date,reserve.is_received,reserve.is_returned))
            con.commit()
    def update_all(self,_users,_books,_reserves):
        for user in _users:
            cur.execute("SELECT * FROM users WHERE national_code=?", (user.national_code,))
            existing_user = cur.fetchone()

            if existing_user:
                cur.execute("UPDATE users SET b_reserve1=? ,b_reserve2=? ,b_reserve3=? ,b_reserve4=? ,b_reserve5=? ,penalty=?, WHERE national_code=?", (user.b_reserve1,user.b_reserve2,user.b_reserve3,user.b_reserve4,user.b_reserve5, user.national_code))
            else:
                cur.execute("INSERT INTO users (national_code, firstname, lastname, username, password,penalty,b_reserve1,b_reserve2,b_reserve3,b_reserve4,b_reserve5,is_admin,) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)",(user.national_code, user.firstname, user.lastname, user.username, user.password,user.penalty,user.b_reserve1,user.b_reserve2,user.b_reserve3,user.b_reserve4,user.b_reserve5,user.is_admin))
            con.commit()

        for book in _books:
            cur.execute("SELECT * FROM books WHERE ID=?", (book.ID,))
            existing_book = cur.fetchone()

            if existing_book:
                continue
            else:
                cur.execute("INSERT INTO books (title, content, publication_year,wrtier,) VALUES (?, ?, ?, ?, ?)",(book.title,book.content,book.publication_year,book.writer))
            con.commit()
        for reserve in _reserves:
            cur.execute("SELECT * FROM reserves WHERE ID=?", (reserve.ID,))
            existing_reserve = cur.fetchone()

            if existing_reserve:
                cur.execute("UPDATE reserves SET start_waiting_date=? ,start_date=? ,end_date=? ,is_received=? ,is_returned=?", (reserve.start_waiting_date,reserve.start_date,reserve.end_date,reserve.is_received,reserve.is_returned))
            else:
                cur.execute("INSERT INTO reserves (applicant, r_book, start_reserve_date, start_waiting_date, start_date, end_date, is_received, is_returned,) VALUES (?, ?, ?, ?, ?, ?, ?, ?,)",(reserve.applicant,reserve.r_book,reserve.start_reserve_date,reserve.start_waiting_date,reserve.start_date,reserve.end_date,reserve.is_received,reserve.is_returned))
            con.commit()

    def last_ID(self,type):
        if(type=="books"):
            index=cur.execute("SELECT LAST INDEX ID() FROM books")
            return index
        elif(type=="reserves"):
            index=cur.execute("SELECT LAST INDEX ID() FROM reserves")
            return index
        else:
            return -1