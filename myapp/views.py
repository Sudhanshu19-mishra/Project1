
from rest_framework. views import APIView
from rest_framework .response import Response
from rest_framework . decorators import api_view
from . models import *
from .serializer import Userserializer
from rest_framework import status


# Create your views here.
class UserViews(APIView):
    def get (self , request , id=None):
        if id : 
            user_obj=User.objects.filter(id=id).first()
            if user_obj:
                serializer= Userserializer(user_obj)
                return Response ({"status": "Success","data":serializer.data})
            else:
                return Response({"error" : "User with Id  Not found"} ,status=404)
        else:
            users=User.objects.all().order_by('-pk')
            serializer=Userserializer(users,many=True)
            return Response({"status": "Success","data":serializer.data})
        
    def post(self, request):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

        # PATCH request
    def patch(self , request , id=None):
        student = User.objects.get(id=id)
        serializer = Userserializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success updated",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

        # DELETE request
    def delete (self, request, id=None) : 
        student = User.objects.get(id=id)
        student.delete()
        return Response({"status": "deleted", "message": "Student was deleted successfully"})

