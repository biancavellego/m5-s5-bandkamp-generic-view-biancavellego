from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwner
from users.serializers import UserSerializer
from rest_framework import generics


# MRO - Method Resolution Order
class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
