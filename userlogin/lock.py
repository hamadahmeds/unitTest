
from user import user 

class lock():

    def __init__(self,lockid, locationid, securitylevel):

        self.lockid=lockid

        self.location=locationid

        self.securitylevel=securitylevel

        self.status="locked"

    def getLockId(self):
       return self.lockid
    def getLocatoinId(self):

        return self.locationid

    def getSecurityLevel(self):

        return self.securitylevel


    def getStatus(self):
        return self.status

    def setStatus(self, status):

        self.status=status

   
def __str__(self):
        return self.lockid + ' ' + self.status