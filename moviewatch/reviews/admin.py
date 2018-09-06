from django.contrib import admin

from .models import Movie, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('movie', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('name',)
    list_filer = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
