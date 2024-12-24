from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.contrib.auth import views as auth_views
from blog.views import default_layout, signup, about

urlpatterns = [
    path('admin/', admin.site.urls),

#  token authentication w/ djoser
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

    path('', default_layout, name='home'),  # 기본 URL
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup, name='signup'),
    path('about/', about, name='about'),  # About 페이지 경로 추가

#  authentication w/ jwt
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),

    path('blog/', include('blog.urls'))
]
