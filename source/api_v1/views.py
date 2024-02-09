from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api_v1.serializers import PublicationModelSerializer
from webapp.models import Publication
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from api_v1.permissions import IsAuthorPermission


class PublicationModelViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationModelSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthorPermission()]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
