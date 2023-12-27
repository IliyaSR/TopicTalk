from django.urls import path, include

from topictalk.post import views

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('details/', views.post_details, name='post-details'),
    path('minecraft/', views.minecraft, name='minecraft')
]
