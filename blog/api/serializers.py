from django.contrib.auth.models import User, Group
from blog.models import Post
from rest_framework.serializers import ModelSerializer


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
                  'author',
                  'title',
                  'text',
                  'created_date',
                  'published_date',
                  'image'
                  ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
                  'id',
                  'author',
                  'title',
                  'text',
                  'created_date',
                  'published_date',
                  'image'
                  ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                  'author',
                  'title',
                  'text',
                  'created_date',
                  'published_date',
                  'image'
                  ]
