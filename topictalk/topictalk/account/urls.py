from django.urls import path, include

from topictalk.account import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.details_profile, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete')
    ]))
]
