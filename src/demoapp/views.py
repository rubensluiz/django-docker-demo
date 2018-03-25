from django.http import HttpResponse
import socket

def index(request):
    hostname = socket.gethostname()
    return HttpResponse(hostname + " - Hello, world! \n")
