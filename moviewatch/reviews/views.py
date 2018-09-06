from django.shortcuts import render, get_object_or_404

from .models import Review, Movie

def movie_list(request):
    movie_list = Movie.objects.order_by('name')
    context = {'movie_list': movie_list}
    return render(request, 'reviews/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'reviews/movie_detail.html', context)

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'reviews/review_detail.html', context)
