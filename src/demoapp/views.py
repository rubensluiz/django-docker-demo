from django.http import HttpResponse
import socket

def index(request):
    return HttpResponse("Hello, world! 2.0\n")
