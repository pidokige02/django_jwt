from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),

    # for REST API
    path('api/', views.posts_api, name='posts_api'),
    path('api/<int:id>/', views.post_detail_api, name='post_detail_api'),
    path('api/create/', views.post_create_api, name='post_create_api'),
    path('api/update/<int:id>/', views.post_update_api, name='post_update_api'),
    path('api/delete/<int:id>/', views.post_delete_api, name='post_delete_api'),

]
