from rest_framework import serializers
from .models import Actor, Movie
from django.utils.text import slugify


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150)
    slug = serializers.SlugField(read_only=True)
    year = serializers.IntegerField(default=1920)
    genre = serializers.CharField()
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)

    def create(self, validated_data):
        actors = validated_data.pop('actors', [])
        title = validated_data.get('title')

        # Slug generation
        origin_slug = slugify(title)
        slug = origin_slug
        count = 0
        while Movie.objects.filter(slug=slug).exists():
            count += 1
            slug = f"{origin_slug}-{count}"

        movie = Movie.objects.create(**validated_data, slug=slug)
        movie.actors.set(actors)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre', instance.genre)

        if 'actors' in validated_data:
            actors = validated_data.pop('actors')
            instance.actors.set(actors)

        instance.save()
        return instance
