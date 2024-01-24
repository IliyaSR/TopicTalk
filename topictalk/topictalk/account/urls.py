from django.urls import path, include

from topictalk.account import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.details_profile, name='profile-details'),
        path('edit/', views.UserEditView.as_view(), name='profile-edit'),
        path('delete/', views.UserDeleteView.as_view(), name='profile-delete')
    ]))
]
