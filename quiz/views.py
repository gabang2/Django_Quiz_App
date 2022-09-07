from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random


@api_view(['GET'])
def helloAPI(request):
    return Response('helo_world!')


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuiz = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuiz, many=True)  # many=True로 하면 다량의 데이터도 직렬화를 수행해줌..!!!
    return Response(serializer.data)
