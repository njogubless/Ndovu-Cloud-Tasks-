import datetime
from django.test import TestCase
from .models import Accountant, Attendance, Employee, Expense, Manager, Project, Technician 


# Create your tests here.
class ManagerTest(TestCase):
    def setUp(self):
        self.manager1 = Manager(name='Paul ',position=" supervisor",department ='ICT ')

    def test_instance(self):
        self.assertTrue(isinstance(self.manager1,Manager))


class ProjectTest(TestCase):
    def setUp(self):
        self.project1 = Project(name='repoertsystem',manager='Paul')

    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Project))

class EmployeeTest(TestCase):
    def setUp(self):
        self.employee1 = Employee(name='Emmanuel',department ='Marketing')

    def test_instance(self):
        self.assertTrue(isinstance(self.employee1,Employee))

class TechnicianTest(TestCase):
    def setUp(self):
        self.technician1 = Technician(name='Joel',department ='ICT ')

    def test_instance(self):
        self.assertTrue(isinstance(self.technician,Technician))


class AttendanceTest(TestCase):
    def setUp(self):
        self.attendance1 = Attendance(employee='Joel',date='May 22nd 2023')

    def test_instance(self):
        self.assertTrue(isinstance(self.attendance1,Attendance))


class AccountantTest(TestCase):
    def setUp(self):
        self.accountant1= Accountant(name=' Martin',department='Finance')
        
        def test_instance(self):
            self.assterTrue(isinstance(self.accountant1,Accountant))


class ExpenseTest(TestCase):
    def setup(self):
        self.expense1= Expense(description='taxes',amount='50,000')

    def test_instance(self):
        self.assertTrue(isinstance(self.expense,Expense))