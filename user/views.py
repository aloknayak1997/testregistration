from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import json
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        print(username)
        print(mobile)
        user = User(username=username,mob_no=int(mobile))
        if user.save():
            response_data ={'Status':True, 'Message': "succesfully added" }
        response_data ={'Status':False, 'Message': "Please recheck your data and try again" }
        return HttpResponse(json.dumps(response_data), content_type="application/json")
