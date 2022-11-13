from dataclasses import field
from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('id', 'name',)
        
class ActorSerializer(serializers.ModelSerializer):
    class ActorMovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('title',)
    
    movies = ActorMovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'
        
class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content',)
        
class ReviewSerializer(serializers.ModelSerializer):
    class ReviewMovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = ReviewMovieSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'overview',)
        
class MovieSerializer(serializers.ModelSerializer):
    class MovieActorSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Actor
            fields = ('name',)
            
    actors = MovieActorSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        