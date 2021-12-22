from django.shortcuts import render
from django.views.generic import CreateView
from core.forms import ShortenerForm
from django.urls import reverse_lazy
from core.models import Shortener
from django.http import HttpResponseRedirect, Http404

def home(request):
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'POST':

        form = ShortenerForm(request.POST)

        if form.is_valid():
            if Shortener.objects.filter(long_url = form.cleaned_data['long_url']).exists():
                context['new_url'] = request.build_absolute_uri('/') + Shortener.objects.filter(long_url = form.cleaned_data['long_url']).first().short_url
                context['old_url'] = Shortener.objects.filter(long_url = form.cleaned_data['long_url']).first().long_url
                context['followed'] = Shortener.objects.filter(long_url = form.cleaned_data['long_url']).first().followed
                context['message'] = 'This URL have already been shorted :)'
            else:
                created_object = form.save()
                context['new_url']  = request.build_absolute_uri('/') + created_object.short_url
                context['old_url'] = created_object.long_url
                context['followed'] = created_object.followed 
             
            return render(request, 'index.html', context)

        context['errors'] = form.errors

        return render(request, 'index.html', context)

    elif request.method == 'GET':
        return render(request, 'index.html', context)


def redirect_view(request, code):

    try:
        shortener = Shortener.objects.get(short_url=code)

        shortener.followed += 1        

        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('This URL is Invalid.')
