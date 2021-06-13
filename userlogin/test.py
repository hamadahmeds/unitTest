import unittest
from lock  import lock
from user  import user
from scan import Scan

class TestLock(unittest.TestCase):
    def setUp(self):
        self.LK=lock(123, 40, 1)
    def test_lockid(self):
       self.assertEqual(self.LK.getLockId(), 123)

    

class Testusername(unittest.TestCase):
    def setUp(self):
         self.name=user('PASS',1 , 'vailid')

    def test_username(self):
         self.assertEqual(self.name.getUserName(),'PASS')


class TestSan(unittest.TestCase):
    def setUp(self):
         self.lock=Scan(1 ,2)

    def test_Scan(self):
         self.assertEqual(self.lock.getLock(), 1)
    def test_card(self):
         self.assertEqual(self.lock.getCard(), 2)
