from django.shortcuts import render

# Create your views here.
def login_fbv(request):
    context = {

    }
    return render(request, 'member/login.html', context)