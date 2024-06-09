from django.shortcuts import render
from .forms import EmployeeCreateForms
def employee_add(request):
    # context = {
    #     "class_name": "Django Class"
    # }
    # return render(request, "demo.html", context)
    emp_create_form = EmployeeCreateForms()
    context = {"form": emp_create_form}
    return render(request, "employees/add_employees.html", context)
def employee_edit(request):
    return render(request, "employees/edit_employees.html")
def employee_index(request):
    return render(request, "employees/index_employees.html")
def employee_show(request):
    return render(request, "employees/show_employees.html")