"""Users views."""
from django.http import HttpResponseForbidden
# Django REST Framework
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from users.models import User
from users.serializers import UserModelSerializer, LoginSerializer, \
    UserSignUpSerializer, CustomTokenObtainPairSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet
                  ):
    """User view set."""
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'list', 'delete']:
            permissions = [IsAuthenticated]
        else:
            permissions = []
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""

        login_serializer = CustomTokenObtainPairSerializer(data=request.data)
        if login_serializer.is_valid():
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.get(**serializer.data)
                user_data = UserModelSerializer(user).data
                user_data['token'] = login_serializer.validated_data.get('access')
                user_data['refresh-token'] = login_serializer.validated_data.get('refresh')
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
        user = User.objects.filter(id=request.user.id)
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Session closed successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
