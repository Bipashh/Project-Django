from django.shortcuts import render

def demo(request):
    context = {
        "class_name": "Django Class"
    }
    return render(request, "demo.html", context)