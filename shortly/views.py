from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    
@login_required(login_url='login')
def tags(request):
    if request.method == "GET":
        return render(request, 'tags.html')
    
@login_required(login_url='login')
def links(request):
    if request.method == "GET":
        return render(request, 'links.html')