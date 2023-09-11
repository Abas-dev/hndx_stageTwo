from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import Person
from .serializers import PersonSerializer

class CreatePerson(GenericAPIView):
    serializer_class = PersonSerializer

    def post(self,request:Request):

        response = {
            'message':'test is working'
        }
        return Response(data=response,status=status.HTTP_201_CREATED)


    def get(self,request:Request):

        response = {
            'message':'test is working'
        }
        return Response(data=response,status=status.HTTP_201_CREATED)