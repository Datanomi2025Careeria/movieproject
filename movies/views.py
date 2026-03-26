from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Genre, Movie
from .forms import GenreForm, MovieForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'movies/register.html', {'form': form})

# GENRE CRUD
@login_required
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'movies/genre_list.html', {'genres': genres})

@login_required
def genre_add(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'movies/genre_form.html', {'form': form})

@login_required
def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genre.delete()
    return redirect('genre_list')

# MOVIE CRUD
@login_required
def movie_list(request):
    movies = Movie.objects.select_related('genre').all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

@login_required
def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')

@login_required
def genre_edit(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'movies/genre_form.html', {'form': form})

@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})