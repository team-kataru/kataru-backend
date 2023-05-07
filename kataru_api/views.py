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


