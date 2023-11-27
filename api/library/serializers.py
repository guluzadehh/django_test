from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    detail_url = serializers.URLField(source="get_absolute_url", read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=models.Author.objects.all())

    class Meta:
        model = models.Book
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        author_serializer = AuthorSerializer(instance.author)
        data["author"] = author_serializer.data
        return data
