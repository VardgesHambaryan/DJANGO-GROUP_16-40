from django.shortcuts import render
from .models import Movie


def home(request):

    movies = Movie.objects.all()
    return render(request , 'index.html', context={
        "movies":movies
    })