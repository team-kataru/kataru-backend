from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, PromptSerializer, UserSerializer
from .models import Genre, Prompt, User

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
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def genres_id(request, pk):
    """
    List, update or delete one genre by id.
    """
    if request.method == 'GET':
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=404)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=404)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
        
    elif request.method == 'DELETE':
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=404)
        genre.delete()
        return Response(status=204)

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
        return Response(serializer.data, status=200)
    
    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def prompts_id(request, pk):
    """
    List, update or delete one prompt by id.
    """
    if request.method == 'GET':
        try:
            prompt = Prompt.objects.get(pk=pk)
        except Prompt.DoesNotExist:
            return Response(status=404)
        serializer = PromptSerializer(prompt)
        return Response(serializer.data, status=200)
    
    elif request.method == 'PATCH':
        try:
            prompt = Prompt.objects.get(pk=pk)
        except Prompt.DoesNotExist:
            return Response(status=404)
        serializer=PromptSerializer(prompt, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        try: 
            prompt = Prompt.objects.get(pk=pk)
        except Prompt.DoesNotExist:
            return Response(status=404)
        prompt.delete()
        return Response(status=204)

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
        return Response(serializer.data, status=200)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def users_id(request, pk):
    """
    List, update or delete one user by id.
    """
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    
    elif request.method == 'PATCH':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        user.delete()
        return Response(status=204)