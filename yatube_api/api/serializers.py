from rest_framework import serializers

from posts.models import Post, Comment, Group, User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "cats")
        ref_name = "ReadOnlyUsers"


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.SlugRelatedField(
        slug_field="title",
        queryset=Group.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "group", "pub_date")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
        read_only_fields = ("post",)
