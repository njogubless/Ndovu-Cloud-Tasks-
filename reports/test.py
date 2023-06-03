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
        manager=Manager.objects.create(name="Paul")
        self.project = Project(name='reportsystem',manager=manager)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

class EmployeeTest(TestCase):
    def setUp(self):
        self.employee = Employee(name='Emmanuel',department ='Marketing')

    def test_instance(self):
        self.assertTrue(isinstance(self.employee,Employee))

class TechnicianTest(TestCase):
    def setUp(self):
        self.technician = Technician(name='Joel',department ='ICT ')

    def test_instance(self):
        self.assertTrue(isinstance(self.technician,Technician))


class AttendanceTest(TestCase):
    def setUp(self):
        employee=Employee.objects.create(name="Joel")

        self.attendance = Attendance(employee=employee,date="2023-06-03")

    def test_instance(self):
        self.assertTrue(isinstance(self.attendance,Attendance))


class AccountantTest(TestCase):
    def setUp(self):
        self.accountant = Accountant(name=' Martin',department='Finance')
        
        def test_instance(self):
            self.assterTrue(isinstance(self.accountant,Accountant))


class ExpenseTest(TestCase):
    def setUp(self):
        self.expense= Expense(description='taxes',amount='50,000')

    def test_instance(self):
        self.assertTrue(isinstance(self.expense,Expense))