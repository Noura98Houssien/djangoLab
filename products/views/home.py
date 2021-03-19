from django.shortcuts import render
from django.http import HttpResponse
from products.models.depart import Department
from products.models.item import Item
# Create your views here.

def index(request):
    # call landing page in dir home/index.html
    # list all Departments
    
    depatments = Department.objects.filter(active=1)
    return render(request, 'home/index.html', {'all_departments' : depatments})

def list_items(request):
    all_items=Item.objects.filter(department=request.POST.get('department'))
    print(all_items)
    print("==========================================")
    return render(request,'home/test.html',{'all_items':all_items})