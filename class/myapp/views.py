from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request,'firstpage.html')
def f2(request):
    return render(request,'secondpage.html')