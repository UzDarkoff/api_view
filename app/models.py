from django.db import models
from django.utils.text import slugify


class Actor(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()


class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True)
    year = models.IntegerField(default=1920)
    actors = models.ManyToManyField(Actor, related_name='actor')
    genre = models.TextField()

    def save(self, **kwargs):
        if not self.slug:
            origin_slug = slugify(self.title)
            slug = origin_slug
            count = 0
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{slug}-{count}"
                count += 1
            self.slug = slug
        super().save(**kwargs)

    def __str__(self):
        return self.title