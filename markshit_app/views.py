from django.shortcuts import render
from .models import student

# Create your views here.
# def home (request):
#     if request.method=='POST':
#         num1=float(request.POST['Hindi'])
#         num2=float(request.POST['English'])
#         num3=float(request.POST['Math'])
#         num4=float(request.POST['Sanskrit'])
#         num5=float(request.POST['Computer'])
#         num6=float(request.POST['Science'])
        

#         if 'add' in request.POST:
#             a=num1+num2+num3+num4+num5+num6
#             return render(request,'home.html',{'sum':a})
#         else:
#             return render(request,'home.html')

def home(request):
    if request.method=='POST':
        num1=int(request.POST['n1'])
        num2=int(request.POST['n2'])
        num3=int(request.POST['n3'])
        num4=int(request.POST['n4'])
        num5=int(request.POST['n5'])
        num6=int(request.POST['n6'])
        sum=num1+num2+num3+num4+num5+num6
        per=(sum/600)*100

        
        return render(request,'home.html',{'sum':sum,'par':per})

        
    else:
         return render(request,'home.html')
        

def show(request):
    data=student.objects.all
    return render(request, 'show.html',{"data":data})

