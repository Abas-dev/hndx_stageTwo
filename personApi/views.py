from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404

from .models import Person
from .serializers import PersonSerializer


class CreatePerson(GenericAPIView):
    serializer_class = PersonSerializer

    def post(self,request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                'message':'test is working',
                'data': serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data={'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class GetAllPerson(GenericAPIView):
    serializer_class = PersonSerializer

    def get(self,request:Request): 
        person = Person.objects.all() 
        serializer = self.serializer_class(instance=person,many=True)

        response = {
            "message": serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

class GetUpdateDeletePerson(GenericAPIView):
    serializer_class = PersonSerializer

    def get(self,request:Request,pk):
        data = get_object_or_404(Person,id=pk)
        serializer = self.serializer_class(instance=data)
        return Response(data={"message":serializer.data},status=status.HTTP_200_OK)

    def put(self,request:Request,pk):
        data_id = get_object_or_404(Person,id=pk)
        data = request.data 
        serializer = self.serializer_class(instance=data_id,data=data) 

        if serializer.is_valid():
            serializer.save()  

            response = {
                "message" : "person updated successfully",
                "data" : serializer.data 
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=response,status=status.HTTP_201_CREATED)

    def delete(self,request:Request,pk):
        data_id = get_object_or_404(Person,id=pk) 
        data_id.delete()
        response = {
            "message":"person was deleted successfully"
        }
        return Response(data=response,status=status.HTTP_204_NO_CONTENT)    