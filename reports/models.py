from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Report(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
   
 
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()

employee=Employee(name="Joel")
employee.save()
print("employee Name;",employee.name)
    

from django.db import models

class Technician(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
   

class Ticket(models.Model):
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    description = models.TextField()
   

from django.db import models

class Accountant(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
   

class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    

