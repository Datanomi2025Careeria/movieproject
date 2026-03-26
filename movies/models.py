from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return f"{self.title} ({self.year})"