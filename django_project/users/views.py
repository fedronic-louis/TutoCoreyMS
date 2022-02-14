from django.shortcuts import render, redirect
# L'import ci-dessous permet si l'on veut créer des "forms" de "scratch", il permettra differents type de validation en allant de l'email au mot de passe en passant par l'insertion d'information correct
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
