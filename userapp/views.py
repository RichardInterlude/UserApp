from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . serializers import UserSerializer, ProfileSerializer, RegistrationSerializer
from django.contrib.auth.models import User

from . models import Profile


class RegistrationView(APIView):
    def post(self,request):
        try:
            serializers = RegistrationSerializer(data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)})







