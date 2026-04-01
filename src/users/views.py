
from django.http import HttpResponse
# Create your views here.

def home_users():
    return HttpResponse(
        "Hello, world. You're at the users home page."
    )