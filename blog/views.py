from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic
from django.template import loader

# Create your views here.

def index(request):
    latest_topic_name = Topic.objects.order_by('-pub_date')[:5]
    context = {
        'latest_topic_name': latest_topic_name,
    }
    return render(request, 'blog/index.html', context)