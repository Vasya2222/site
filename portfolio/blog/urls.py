
from django.urls import path, include
from . import views

app_name = 'blog_id'

urlpatterns = [
    path('personal_blog', views.blog, name='blog'),
    path('<int:id_blog>', views.detail, name='detail')
]