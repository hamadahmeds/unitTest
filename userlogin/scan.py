from lock import lock
import datetime

class Scan():
    def __init__(self, lock, card):

        self.lock=lock
        self.card=card
        # self.datetime.date.tody()
        # self.time=datetime.time.strftime()

    def getLock(self):
        
        return self.lock

    def getCard(self):
        
        return self.card
        
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time

