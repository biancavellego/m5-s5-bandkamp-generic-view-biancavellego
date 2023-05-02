from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404

from users.models import User


class CreateBaseView:
    def create(self, request: Request) -> Response:
        """
        Registro de usuários
        """
        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveBaseView:
    def retrieve(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """
        Obtençao de usuário
        """
        url_param = kwargs.get(self.url_params_name)
        object = get_object_or_404(self.view_queryset, pk=url_param)

        self.check_object_permissions(request, object)
        serializer = self.view_serializer(object)

        return Response(serializer.data)


class UpdateBaseView:
    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """
        Atualização de usuário
        """
        url_param = kwargs.get(self.url_params_name)
        object = get_object_or_404(self.view_queryset, pk=url_param)

        self.check_object_permissions(request, object)
        serializer = self.view_serializer(object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class DestroyBaseView:
    def destroy(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """
        Deleçao de usuário
        """
        url_param = kwargs.get(self.url_params_name)
        object = get_object_or_404(User, pk=url_param)

        self.check_object_permissions(request, object)
        object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
