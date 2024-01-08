from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from topictalk.common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:post_id>/', views.like_functionality, name='like'),
    path('like/comment/<int:comment_id>', views.like_functionality_about_comments, name='like_comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
