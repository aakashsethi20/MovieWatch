import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Review, Movie
from .forms import ReviewForm

def movie_list(request):
    movie_list = Movie.objects.order_by('name')
    context = {'movie_list': movie_list}
    return render(request, 'reviews/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm()
    context = {'movie': movie, 'form': form}
    return render(request, 'reviews/movie_detail.html', context)

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'reviews/review_detail.html', context)

def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['user_name']
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        review = Review()
        review.movie = movie
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()

        # Should return HttpResponseRedirect with POST data to avoid posting
        # twice if the user clicks browser's back button
        return HttpResponseRedirect(reverse('reviews:movie_detail', args=(movie.id,)))

    context = {'movie': movie, 'form': form}
    return render(request, 'reviews/movie_detail.html', context)
