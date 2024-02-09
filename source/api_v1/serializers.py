from django.contrib.auth import get_user_model
from rest_framework import serializers

from webapp.models import Publication


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class PublicationModelSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)

    class Meta:
        model = Publication
        fields = ['id', 'picture', 'description', 'author']
        read_only_fields = ['author']
