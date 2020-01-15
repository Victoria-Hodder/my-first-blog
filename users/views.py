from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save() #saves the users data - hashes password automatically
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Your account has been created. You may now login') #import messages
    #         return redirect('login') #name of url path
    # else:
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})