from rest_framework.views import Request, Response
from utils.base_views import (
    CreateBaseView,
    RetrieveBaseView,
    UpdateBaseView,
    DestroyBaseView,
)
from utils.generic_views import GenericBaseView


class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request: Request) -> Response:
        return super().create(request)


class RetrieveUpdateDestroyGenericView(
    RetrieveBaseView, UpdateBaseView, DestroyBaseView, GenericBaseView
):
    def get(self, request: Request) -> Response:
        return super().retrieve(request)

    def patch(self, request: Request) -> Response:
        return super().update(request)

    def delete(self, request: Request) -> Response:
        return super().destroy(request)
