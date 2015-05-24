from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.rating)


class Projection(models.Model):
    movie_id = models.ForeignKey(Movie)
    pr_type = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return "{} - {} - {}".format(self.movie_id.name, self.pr_type, self.time.time())


class Reservation(models.Model):
    username = models.CharField(max_length=100, unique=True)
    proj_id = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()
