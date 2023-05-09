from django.contrib.auth import get_user_model
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserUploadSerializer

User = get_user_model()


class UserDocUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, format=None):
        serializer = UserUploadSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK, context_instance=RequestContext(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        query_set = User.objects.get(pk=request.user)
        serializer = UserUploadSerializer(query_set)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK, context_instance=RequestContext(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """@csrf_exempt
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserUploadSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

    """def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
