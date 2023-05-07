from rest_framework import serializers
from .models import Genre, Prompt, User

"""Create CRUD serializers for each model"""

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('level', 'category', 'created_at', 'updated_at')

        def create(self, validated_data):
            return Genre.objects.create(**validated_data)
        
        def retrieve(self, instance):
            return instance
        
        def update(self, instance, validated_data):
            instance.level = validated_data.get('level', instance.level)
            instance.category = validated_data.get('category', instance.category)
            instance.updated_at = validated_data.get('updated_at', instance.updated_at)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ('prompt_text', 'genre', 'created_at', 'updated_at')

        def create(self, validated_data):
            return Prompt.objects.create(**validated_data)
        
        def retrieve(self, instance):
            return instance
        
        def update(self, instance, validated_data):
            instance.prompt_text = validated_data.get('prompt_text', instance.prompt_text)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.updated_at = validated_data.get('updated_at', instance.updated_at)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()

            