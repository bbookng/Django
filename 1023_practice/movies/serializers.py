from dataclasses import field
from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('id', 'name',)
        
class ActorSerializer(serializers.ModelSerializer):
    
    movies = MovieTitleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'
        
class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content',) 
        
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    
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
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'