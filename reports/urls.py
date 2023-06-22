from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name='home'),
    path('department/<int:department_id>/', department_report, name='department_report'),
    #path('report/<int:report_id>/', report detail, name='report_details'),
    path('report/create/', create_report, name='create_report'),
]