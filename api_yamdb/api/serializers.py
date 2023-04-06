from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from reviews.validators import (validate_title_year, validate_user_username,
                                validate_username_regexp)
from users.models import User


class UserEmailRegistration(serializers.Serializer):
    email = serializers.EmailField(required=True,
                                   max_length=254,
                                   )
    username = serializers.CharField(required=True,
                                     max_length=150,
                                     validators=[validate_username_regexp(),
                                                 validate_user_username]
                                     )

    def validate(self, value):
        user1 = User.objects.filter(email=value['email'])
        if user1.exists():
            if not User.objects.filter(username=value['username']).exists():
                raise serializers.ValidationError(
                    'Вы не можете зарегистрировать другое имя на эту почту')
        user2 = User.objects.filter(username=value['username'])
        if user2.exists():
            if not User.objects.filter(email=value['email']).exists():
                raise serializers.ValidationError(
                    'Вы не можете зарегистрировать другую почту на это имя')
        return value


class UserConfirmation(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio',
                  'role'
                  )


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description',
            'genre', 'category', 'rating'
        )

    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return obj.reviews.all().aggregate(Avg('score'))['score__avg']


class TitleSerializerCrUpDel(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')
    year = serializers.IntegerField(validators=[validate_title_year])

    class Meta:
        model = Title
        fields = ('id', 'name', 'year',
                  'description', 'genre', 'category'
                  )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = (
            'id', 'text', 'author',
            'score', 'pub_date', 'title'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'text', 'author', 'pub_date')
