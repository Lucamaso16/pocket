from django.shortcuts import render

def general(request):
    return render(request, 'scambi/general.html')
