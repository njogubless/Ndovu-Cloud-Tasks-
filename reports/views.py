from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Report
from report_system.forms import ReportForm

def home(request):
    departments = Department.objects.all()
    return render(request, 'report_system/home.html', {'departments': departments})

def department_report(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    reports = Report.objects.filter(department=department)
    return render(request, 'report_system/department_report.html', {'department': department, 'reports': reports})
def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            return redirect('report_details', report_id=report.id)
    else:
        form = ReportForm()
    return render(request, 'report_system/create_report.html', {'form': form})



# Create your views here.
