from django.shortcuts import render

def employee_add(request):
    # context = {
    #     "class_name": "Django Class"
    # }
    # return render(request, "demo.html", context)
    return render(request, "employees/add_employees.html")
def employee_edit(request):
    return render(request, "employees/edit_employees.html")
def employee_index(request):
    return render(request, "employees/index_employees.html")
def employee_show(request):
    return render(request, "employees/show_employees.html")