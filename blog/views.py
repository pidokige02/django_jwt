from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.timezone import now
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .services.jwt_service import fetch_jwt_token
from .models import Post
from .forms import SignUpForm, PostCreateForm
from .serializers import PostSerializer


# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))
# for local application only
@login_required  # 로그인된 사용자만 접근 가능
def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'blog/posts.html', {'posts': posts})

# for frontend only
@api_view(['GET'])
def posts_api(request):
    if request.method == 'GET':
        posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
        posts_data = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at,
                'updated_at': post.updated_at,
                'published_at': post.published_at,
                'author': post.author.username,  # 작성자 이름 포함
            } for post in posts
        ]
        return JsonResponse(posts_data, safe=False)

# for local application only
def default_layout(request):
    # 전달할 컨텍스트 데이터 (필요한 경우)
    context = {
        "title": "Default Layout",
        "message": "Welcome to the Default Layout Page",
    }
    return render(request, "blog/home.html", context)

# for local application only
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

# for local application only
def about(request):
    return render(request, 'blog/about.html')  # about.html 템플릿을 렌더링

# for local application only
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# for frontend only
@api_view(['GET'])
def post_detail_api(request, id):
    # 게시물을 가져오거나 404 오류 반환
    post = get_object_or_404(Post, id=id)

    # 게시물 데이터를 JSON 형식으로 변환
    post_data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at,
        'updated_at': post.updated_at,
        'published_at': post.published_at,
        'author': post.author.username,  # 작성자 이름 포함
    }

    # JSON 응답 반환
    return JsonResponse(post_data)

# for local application only
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_create.html', {'form': form})


# for frontend only
@csrf_exempt  # Vue.js에서 CSRF 토큰 없이 요청할 경우 필요
@api_view(['POST'])
def post_create_api(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(author=request.user, published_at=now())
            return Response({'id': post.id, 'message': 'Post created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)