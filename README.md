# 1. About my Sample Project
My sample project is baiscally a Report_System where departments in an Organization will have a more efficient way of providing reports for the work they have achived.

As most tech comapnies have standups to have a review of work done and challenges experienced by various developers, this particular sample project was aimed to provide space for a more detailed explanation of what departments have been able to cover. 

# What has been covered. 

By the use of the Travis CI I have runned a couple of unit test on the models I had and through the test.py file I was able to debug some code and add partcular instances in my test.py.

All the 6 tests for the models I had runned successfuly using the 
'''
python language

 python manage.py test" command 
 '''
~~~
import datetime
from django.test import TestCase
from .models import Accountant, Attendance, Employee, Expense, Manager, Project, Technician 


# this is a code snippet of the tests created.
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

~~~

# Configurations
I have had issues with various configuration files that was to enable me successfully deploy my appliaction and as well conecct it to the host server.
# this is the nginx.conf file
~~~
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 768;
    # multi_accept on;
}

http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
