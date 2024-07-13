from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    lowercase = request.GET.get('lowercase')
    symbols = request.GET.get('symbols')
    if length < 8:
        return render(request, 'password.html', {'error': 'Password length must be at least 8 characters'})
    else:
        password = generate_password(length, uppercase, lowercase, symbols)
        return render(request, 'password.html', {'password': password})
