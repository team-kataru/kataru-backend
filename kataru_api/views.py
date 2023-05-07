from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer
from .models import Genre, Prompt, User

"""
Test View
"""

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

"""
Genres View
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
