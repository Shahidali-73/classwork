from django.shortcuts import render, get_object_or_404, redirect
from .models import Library
from .forms import LibraryForm


def library_add_book(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library')
    else:
        form = LibraryForm()
    return render(request, 'add.html', {'form': form})


def library_read(request):
    product_list = Library.objects.all()
    return render(request, 'retrieve.html', {'product_list': product_list})


def library_update(request, id):
    product = get_object_or_404(Library, pk=id)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('library')
    else:
        form = LibraryForm(instance=product)
    return render(request, 'update.html', {'form': form})


def library_delete(request, pk):
    product = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('library')
    return render(request, 'delete.html', {'library': product})



