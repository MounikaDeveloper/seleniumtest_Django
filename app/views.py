from django.shortcuts import render
from app.models import Register
# Create your views here.
def showIndex(request):
    return render(request,'index.html')


def welcomePage(request):
    fname=request.POST['fname']
    lname = request.POST['lname']
    pnumber= request.POST['pnumber']
    Register(fname=fname,lname=lname,phonenumber=pnumber).save()
    return render(request,'welcome.html')