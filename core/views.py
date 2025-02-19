from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hellotime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>Hello, world!</h1><p>It's {now}</p>")

def screenprint(request):
    return render(request, "core/screenprint.html")







# Create your views here.
# best site ever
