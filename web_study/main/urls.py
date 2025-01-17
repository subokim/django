from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting, new_post, remove_post

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('blog/',blog, name='blog'),
    path('blog/<int:pk>',posting, name='posting'),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)