from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse


def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({"message": "Signup successful"}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse({"message": "Login successful"}, status=200)
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=401)