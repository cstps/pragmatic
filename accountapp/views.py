from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
  # return HttpResponse('hello world')
  if request.method =="POST":
    return render(request, 'accountapp/hello_world.html', context={'text':'POST Method'})
  else:
    return render(request, 'accountapp/hello_world.html', context={'text':'GET Method'})