from django.urls import path, include

from topictalk.post import views

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('details/<int:pk>/', views.post_details, name='post-details'),
    path('minecraft/', views.minecraft, name='minecraft'),
    path('league_of_legends/', views.league_of_legends, name='League of Legends'),
    path('nba/', views.nba, name='nba'),
    path('premier_league/', views.premier_league, name='premier-league'),
    path('bitecoin/', views.bitecoin, name='bitecoin'),
    path('litecoin/', views.litecoin, name='litecoin'),
    path('comment/<int:post_id>/', views.add_comment, name='comment'),
    path('delete/<int:post_id>/', views.delete_post, name='delete-post'),
    path('delete_comment/<int:comment_id>/<int:post_id>/', views.delete_comment, name='delete-comment')
]
