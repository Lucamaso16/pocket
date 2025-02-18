from django.shortcuts import render
from accounts.models import CustomUser

def general(request):
    return render(request, 'scambi/general.html')

def users_list(request):
    users = CustomUser.objects.filter(is_superuser=False)
    return render(request, 'scambi/users_list.html', {'users': users})