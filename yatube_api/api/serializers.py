from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    group = serializers.SlugRelatedField(read_only=True,
                                         slug_field='title')

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group',
                  'comments')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'posts')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        model = Comment
        read_only_fields = ('author', 'post')
