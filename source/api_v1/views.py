from rest_framework import status
from rest_framework.decorators import action
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

    @action(detail=True, methods=['post', 'delete'])
    def like_unlike(self, request, pk=None):
        publication = self.get_object()
        if request.method == 'POST':
            publication.likes.add(request.user)
            return Response({'detail': 'Лайк успешно добавлен.'}, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            publication.likes.remove(request.user)
            return Response({'detail': 'Лайк успешно удален.'}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
