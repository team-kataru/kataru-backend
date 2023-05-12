from rest_framework import serializers
from .models import Genre, Prompt, User, Entry, Story, PromptRegistry

"""
Create CRUD serializers for each model
"""

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'level', 'category', 'created_at', 'updated_at')

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
        fields = ('id', 'prompt_text', 'genre', 'created_at', 'updated_at')

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user_name', 'password', 'email', 'created_at', 'updated_at')

        def create(self, validated_data):
            return User.objects.create(**validated_data)
        
        def retrieve(self, instance):
            return instance
        
        def update(self, instance, validated_data):
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.user_name = validated_data.get('user_name', instance.user_name)
            instance.password = validated_data.get('password', instance.password)
            instance.email = validated_data.get('email', instance.email)
            instance.updated_at = validated_data.get('updated_at', instance.updated_at)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()
    
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'entry_text', 'user_id', 'story_id', 'genre_id', 'prompt_id', 'created_at', 'updated_at')

        def create(self, validated_data):
            return Entry.objects.create(**validated_data)
        
        def retrieve(self, instance):
            return instance
        
        def update(self, instance, validated_data):
            instance.entry_text = validated_data.get('entry_text', instance.entry_text)
            instance.user_id = validated_data.get('user_id', instance.user_id)
            instance.story_id = validated_data.get('story_id', instance.story_id)
            instance.genre_id = validated_data.get('genre_id', instance.genre_id)
            instance.prompt_id = validated_data.get('prompt_id', instance.prompt_id)
            instance.updated_at = validated_data.get('updated_at', instance.updated_at)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'user_id', 'genre_id', 'created_at', 'updated_at')

        def create(self, validated_data):
            return Story.objects.create(**validated_data)
        
        def retrieve(self, instance):
            return instance
        
        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.user_id = validated_data.get('user_id', instance.user_id)
            instance.genre_id = validated_data.get('genre_id', instance.genre_id)
            instance.updated_at = validated_data.get('updated_at', instance.updated_at)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()

class PromptRegistrySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    prompt = PromptSerializer()

    class Meta:
        model = PromptRegistry
        fields = '__all__'
        # fields = ('id', 'user_id', 'prompt_id')