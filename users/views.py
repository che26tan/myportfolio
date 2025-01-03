from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('firstname')
        password = request.POST.get('pd')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('firstname')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        gen = request.POST.get('gender')
        password = request.POST.get('pd')
        user_email = request.POST.get('uemail')
        ph = request.POST.get('uphone')

    return render(request, 'signup.html')


def profile(request):
    return render(request,'profile.html')