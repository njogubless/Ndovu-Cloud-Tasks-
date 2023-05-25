from django.test import TestCase
from .models import Manager 


# Create your tests here.
class ManagerTest(TestCase):
    def setUp(self):
        self.manager1 = Manager(name='Paul ',position=" supervisor",department ='ICT ')

    def test_instance(self):
        self.assertTrue(isinstance(self.manager1,Manager))