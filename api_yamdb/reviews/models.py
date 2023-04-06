from datetime import datetime
from django.core.validators import (MaxValueValidator,
                                    RegexValidator,
                                    MinValueValidator)
from django.db import models
from django.db.models import Avg

from users.models import User

SLUG_VALIDATOR = RegexValidator(r'^[-a-zA-Z0-9_]+$')


class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[SLUG_VALIDATOR]
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[SLUG_VALIDATOR]
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[
            MaxValueValidator(
                datetime.now().year, message='год выпуска не может быть больше'
                                             ' текущего')]
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category',
    )
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']

    def average_rating(self):
        return self.reviews.aggregate(Avg('score'))['rating']

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title_id = models.ForeignKey(
        Title, db_column='title_id', on_delete=models.CASCADE)
    genre_id = models.ForeignKey(
        Genre, db_column='genre_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_id} {self.genre_id}'


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[MaxValueValidator(10),
                    MinValueValidator(1)]
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.title}, оценка: {self.score}'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review_id = models.ForeignKey(
        Review, db_column='review_id', on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'автор: {self.author}, коммент: {self.text}'
