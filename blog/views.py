from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from .models import Article

def home(request):
    context = {
        "articles": Article.objects.filter(status="p").order_by('-publish')
    }
    return render(request, "blog/home.html", context)
