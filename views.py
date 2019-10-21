from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect

def Thankview(request):
    return render(request,'MyApp/thanks.html')

def User_View(request):
    if request.method  == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Bye')
    else:
        form = forms.UserForm()
    return render(request,'MyApp/Welcome.html', {'form':form})