from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ipware.ip import get_client_ip

from requests import get

# Create your views here.
# def index(request):
#     template = loader.get_template('hello_world/index.html')
#     context = {
#         'greeting': 'Hello Overlord!!',
#     }
#     return HttpResponse(template.render(context, request))

# Or we use a render
def index(request):
    # print(request.META)
    # ip = request.META.get('HTTP_X_CLIENT_IP') # Get client IP

    ip = get('https://api.ipify.org').text
    print(f'My public IP address is: {ip}')

    print(ip)
    context = {
        'greeting': 'Hello Overlord!!',
        'my_ip': ip,
    }
    return render(request, 'index.html', context)