from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'Rizwan Khan'}
    return render(request, 'index.html', params)

def addUser(request):
    print(request.POST)
    params = request.POST.get('name','default')
    print(params)
    return HttpResponse("jj")
    # return render(request, 'index.html', params)

