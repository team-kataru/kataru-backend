from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GenreSerializer, PromptSerializer, UserSerializer, EntrySerializer, StorySerializer, PromptRegistrySerializer
from .models import Genre, Prompt, User, Entry, Story, PromptRegistry

"""
Test View
"""
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

"""
Genres Views
"""
@api_view(['GET', 'POST'])
def genres(request):
    """
    List all genres or create a new genre.
    """
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def genres_id(request, pk):
    """
    List, update or delete one genre by id.
    """
    if request.method == 'GET':
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
Prompts Views
"""
@api_view(['GET', 'POST'])
def prompts(request):
    """
    List all prompts or create a new prompt.
    """
    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def prompts_id(request, pk):
    """
    List, update or delete one prompt by id.
    """
    if request.method == 'GET':
        try:
            prompt = Prompt.objects.get(pk=pk)
        except Prompt.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PromptSerializer(prompt)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        try:
            prompt = Prompt.objects.get(pk=pk)
        except Prompt.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=PromptSerializer(prompt, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try: 
            prompt = Prompt.objects.get(pk=pk)
        except Prompt.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        prompt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
Users Views
"""
@api_view(['GET', 'POST'])
def users(request):
    """
    List all users or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def users_id(request, pk):
    """
    List, update or delete one user by id.
    """
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_prompts(request, user_id):
    """
    List all prompts per user id.
    """
    user_id = User.objects.get(id=user_id)
    user_prompts = PromptRegistry.objects.filter(user_id=user_id)
    serializer = PromptRegistrySerializer(user_prompts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_entries(request, user_id):
    """
    List all user entries by user id.
    """
    user_id = User.objects.get(id=user_id)
    user_entries = Entry.objects.filter(user_id=user_id)
    serializer = EntrySerializer(user_entries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_stories(request, user_id):
    """
    List all user stories by user id.
    """
    user_id = User.objects.get(id=user_id)
    user_stories = Story.objects.filter(user_id=user_id)
    serializer = StorySerializer(user_stories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
"""
Entries Views
"""
@api_view(['GET', 'POST'])
def entries(request):
    """
    List all entries or create a new entry
    """
    if request.method == 'GET':
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def entries_id(request, pk):
    """
    List, update or delete one entry by id.
    """
    if request.method == 'GET':
        try:
            entry = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EntrySerializer(entry)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        try:
            entry = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EntrySerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            entry = Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
Stories Views
"""
@api_view(['GET', 'POST'])
def stories(request):
    """
    List all stories or create a new story.
    """
    if request.method == 'GET':
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def stories_id(request, pk):
    """
    List, update or delete one story by id.
    """
    if request.method == 'GET':
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StorySerializer(story)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StorySerializer(story, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    