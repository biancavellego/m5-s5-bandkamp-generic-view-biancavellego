from rest_framework.views import APIView, Request, Response
from base_views import CreateBaseView, RetrieveBaseView, UpdateBaseView, DestroyBaseView


class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None
    url_params_name = "pk"


# Here were connect with the route:
class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request: Request) -> Response:
        # super() references the father class:
        return super().create(request)


class RetrieveGenericView(RetrieveBaseView, GenericBaseView):
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().retrieve(request, *args, **kwargs)


class UpdateGenericView(UpdateBaseView, GenericBaseView):
    def patch(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().update(request, *args, **kwargs)


class DestroyGenericView(DestroyBaseView, GenericBaseView):
    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().destroy(request, *args, **kwargs)
