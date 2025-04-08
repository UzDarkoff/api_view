from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Actor, Movie
from django.utils.text import slugify

class MovieCreateSerializer(serializers.ModelSerializer):
    actor_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Movie
        fields = ['id', 'name', 'year', 'photo', 'genre', 'actor_ids']

    def create(self, validated_data):
        actor_ids = validated_data.pop('actor_ids', [])
        movie = Movie.objects.create(**validated_data)
        if actor_ids:
            actors = Actor.objects.filter(id__in=actor_ids)
            movie.actor.set(actors)
        return movie




