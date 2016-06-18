from django.shortcuts import render
from django.utils import timezone
from .models import Scklk
from .models import Hrkt
# Create your views here.

def post_list(request):     
    posts = Hrkt.objects.all()
    return render(request, 'blog/post_list.html', {})
