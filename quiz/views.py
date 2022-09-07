from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer

@api_view(['GET'])
def helloAPI(request):
    return Response('helo_world!')

