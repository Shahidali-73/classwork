from django.shortcuts import render
from .forms import MovielForm
def movies(request):
    if request.method == 'POST':
        form = MovielForm(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'form-data.html',{
                'message': 'Data saved to db',
                'flm': cust
            })
    else:
        form = MovielForm()
    return render(request,'index.html',{'form':form})
    

# Create your views here.
