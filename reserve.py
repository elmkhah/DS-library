from user import*
from book import*

class reserve:
    def __init__(self,applicant=None,r_book=None,start_reserve_date=None,start_waiting_date=None,start_date=None,end_date=None,is_received=False,is_returned=False):
        self.applicant=applicant
        self.r_book=r_book
        self.start_reserve_date=start_reserve_date
        self.start_waiting_date=start_waiting_date
        self.start_date=start_date
        self.end_date=end_date
        self.is_received=is_received
        self.is_returned=is_returned

    