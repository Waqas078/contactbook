from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Contact
from.form import *
from django.db.models import Q



def home_view(request):
    if request.user.is_authenticated:
        return redirect('contact_list')
    return render(request, 'home.html')

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_list.html', {'contacts': contacts})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, 'Contact created successfully.')
            return redirect('contact_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form, 'title': 'Add Contact'})

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successfully.')
            return redirect('contact_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form, 'title': 'Edit Contact'})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})

@login_required
def contact_search(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query),
            user=request.user
        )
        if not contacts:
            messages.info(request, f'No contacts found for "{query}".')
    else:
        contacts = Contact.objects.filter(user=request.user)
    return render(request, 'search_results.html', {'contacts': contacts, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('contact_list')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()  

    return render(request, 'registration/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect("/login/")