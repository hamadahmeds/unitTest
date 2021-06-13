
class user():
            def __init__(self,username,userid,loginstatus):
       
                 self.username=username
                 self.userid=userid
                 self.loginstatus=loginstatus
                 self.logindate='today'
            def getUserName(self):
                return self.username

            def getUserId(self):
                return self.userid
    
            def setLoginStatus(self):
                return self.loginstatus
            
            def __str__(self):
                return self.itemname