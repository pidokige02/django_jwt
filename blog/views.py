from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, redirect
from django.contrib.auth import login

from .services.jwt_service import fetch_jwt_token
from .models import Post
from .forms import SignUpForm


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")


def get_jwt_token(request):
    username = "admin"
    password = "64105379"

    try:
        response = fetch_jwt_token(username, password)
        if response.status_code == 200:
            return JsonResponse(response.json(), status=200)
        else:
            return JsonResponse({
                "error": f"Failed to obtain token. Status code: {response.status_code}",
                "details": response.text
            }, status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": "An error occurred", "details": str(e)}, status=500)


def default_layout(request):
    # 전달할 컨텍스트 데이터 (필요한 경우)
    context = {
        "title": "Default Layout",
        "message": "Welcome to the Default Layout Page",
    }
    return render(request, "blog/home.html", context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 자동으로 로그인 처리
            return redirect('home')  # 홈 페이지로 리다이렉트
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})