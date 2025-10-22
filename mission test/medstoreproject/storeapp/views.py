from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Medicine
from .forms import MedicineForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm

MAX_MEDICINES_PER_USER = 5

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful.')
            return redirect('medicine_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('medicine_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('login')

@login_required
def medicine_list(request):
    q = request.GET.get('q', '')
    medicines = Medicine.objects.filter(owner=request.user)
    if q:
        medicines = medicines.filter(Q(name__icontains=q) | Q(description__icontains=q))
    paginator = Paginator(medicines, 5)   # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine_list.html', {'page_obj': page_obj, 'q': q})

@login_required
def medicine_create(request):
    current_count = Medicine.objects.filter(owner=request.user).count()
    if current_count >= MAX_MEDICINES_PER_USER:
        messages.error(request, f'You can add only {MAX_MEDICINES_PER_USER} medicines.')
        return redirect('medicine_list')

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            med = form.save(commit=False)
            med.owner = request.user
            med.save()
            messages.success(request, 'Medicine added.')
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicine_form.html', {'form': form, 'create': True})

@login_required
def medicine_edit(request, pk):
    med = get_object_or_404(Medicine, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=med)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine updated.')
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=med)
    return render(request, 'medicine_form.html', {'form': form, 'create': False})

@login_required
def medicine_delete(request, pk):
    med = get_object_or_404(Medicine, pk=pk, owner=request.user)
    if request.method == 'POST':
        med.delete()
        messages.success(request, 'Medicine deleted.')
        return redirect('medicine_list')
    return render(request, 'confirm_delete.html', {'object': med})
