from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.entities.urltag import URLTag

@login_required(login_url='login')
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    
@login_required(login_url='login')
def tags(request):
    user_tags = URLTag.objects.filter(user=request.user)

    if request.method == 'POST' and 'create_tag' in request.POST:
        name = request.POST.get('name')
        if name:
            URLTag.objects.create(name=name, user=request.user)
        return redirect('tags')

    if request.method == 'POST' and 'edit_tag' in request.POST:
        tag_id = request.POST.get('tag_id')
        new_name = request.POST.get('new_name')
        tag = URLTag.objects.filter(id=tag_id, user=request.user).first()
        if tag and new_name:
            tag.name = new_name
            tag.save()
        return redirect('tags')

    if request.method == 'POST' and 'delete_tag' in request.POST:
        tag_id = request.POST.get('tag_id')
        URLTag.objects.filter(id=tag_id, user=request.user).delete()
        return redirect('tags')

    return render(request, 'tags.html', {'tags': user_tags})
    

@login_required(login_url='login')
def links(request):
    if request.method == "GET":
        return render(request, 'links.html')