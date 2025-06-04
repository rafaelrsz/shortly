from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.entities.urltag import URLTag
from core.utils import generate_short_code
from core.entities.shorturl import ShortURL
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from core.entities.click import Click

@login_required(login_url='login')
def home(request):
    tags = URLTag.objects.filter(user=request.user)

    if request.method == "POST":
        original_url = request.POST.get("original_url")
        tag_id = request.POST.get("tag_id")

        if original_url and tag_id:
            short_code = generate_short_code()
            while ShortURL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()

            short_url = ShortURL.objects.create(
                original_url=original_url,
                short_code=short_code,
                user=request.user
            )
            tag = URLTag.objects.filter(id=tag_id, user=request.user).first()
            if tag:
                short_url.tags.add(tag)

            return render(request, 'home.html', {
                'tags': tags,
                'short_code': short_url.short_code
            })

    return render(request, 'home.html', {'tags': tags})


def redirect_short_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code, is_active=True)

    # Registrar clique
    Click.objects.create(
        short_url=short_url,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        referrer=request.META.get('HTTP_REFERER', '')
    )

    return HttpResponseRedirect(short_url.original_url)

    
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
    user_links = ShortURL.objects.filter(user=request.user).prefetch_related('tags')
    
    for link in user_links:
        link.clicks_count = Click.objects.filter(short_url=link).count()
    
    if request.method == 'POST' and 'delete_link' in request.POST:
        link_id = request.POST.get('link_id')
        ShortURL.objects.filter(id=link_id, user=request.user).delete()
        return redirect('links')

    base_url = request.build_absolute_uri('/')[:-1] 
    
    return render(request, 'links.html', {
        'links': user_links,
        'base_url': base_url
    })