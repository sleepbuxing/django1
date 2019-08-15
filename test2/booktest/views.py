from django.shortcuts import render
from booktest.models import *

# Create your views here.
def index(request):
    list = BookInfo.books1.filter(heroinfo__hconment__contains='八')
    context = {'list': list}
    return render(request, 'booktest/index.html', context)