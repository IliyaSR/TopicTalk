from django.urls import path, include

from topictalk.common import views

urlpatterns = [
    path('', views.home, name='home'),
]
