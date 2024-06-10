from django.shortcuts import render, redirect
from .forms import EmployeeCreateForms
from .models import Employee, User, Department
def employee_add(request):
    emp_create_form = EmployeeCreateForms()
    context = {"form": emp_create_form}

    if request.method == "POST":
        emp = Employee()

        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id = request.POST.get('department'))

        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST['address']
        emp.blood_group = request.POST.get('blood_group')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.gender = request.POST.get('gender')
        emp.join_date = request.POST.get('join_date')
        emp.department = department
        emp.user = user
        emp.save()
        return redirect('emp-index')
    return render(request, "employees/add_employees.html", context)
def employee_edit(request):
    return render(request, "employees/edit_employees.html")
def employee_index(request):
    employee_list = Employee.objects.all()
    context = {"data": employee_list}
    return render(request, "employees/index_employees.html", context)
def employee_show(request):
    return render(request, "employees/show_employees.html")