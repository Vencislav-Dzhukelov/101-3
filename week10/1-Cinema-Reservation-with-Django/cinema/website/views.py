from django.shortcuts import render
from .models import Movie, Projection

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    projections = Projection.objects.all()
    return render(request, 'index.html', locals())
