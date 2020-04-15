from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from . import models
from .serializers import UserSignUpSerializer, KeyValuePairSerializer, KeyFilePairSerializer

class LogInView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user': user.username
        })

class UserSignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer



class KeyValuePairView(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = KeyValuePairSerializer
    queryset = models.KeyValuePair.objects

class KeyFilePairView(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = KeyFilePairSerializer
    queryset = models.KeyFilePair.objects



