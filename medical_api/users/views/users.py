"""Users views."""
from django.http import HttpResponseForbidden
# Django REST Framework
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Models
from users.models import User
from users.serializers import UserModelSerializer, LoginSerializer, UserSignUpSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet
                  ):
    """User view set."""
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(**serializer.data)
            user_data = UserModelSerializer(user).data
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return HttpResponseForbidden("Invalid user parameters")

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        pass
