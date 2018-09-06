from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/add_review', views.add_review, name='add_review'),
    path('reviews', views.review_list, name='review_list'),
    path('reviews/<int:review_id>', views.review_detail, name='review_detail'),
]
