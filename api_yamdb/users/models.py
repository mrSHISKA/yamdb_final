from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint

from reviews.validators import validate_username_regexp

ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ'),
)


class User(AbstractUser):
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=150,
        choices=ROLES,
        default='user'
    )
    confirmation_code = models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=150, unique=True,
                                validators=[validate_username_regexp()]
                                )
    email = models.EmailField(max_length=254, unique=True, blank=False)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    class Meta:
        constraints = [
            CheckConstraint(
                name='username_not_me', check=~Q(username__iexact="me")
            ),
            UniqueConstraint(
                name='unique_user_email_pair', fields=['username', 'email']
            ),
        ]
