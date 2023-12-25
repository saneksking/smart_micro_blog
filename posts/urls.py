from posts import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]
