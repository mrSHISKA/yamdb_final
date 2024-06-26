from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, get_jwt_token,
                    send_confirmation_code)

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)
v1_router.register(r'titles', TitleViewSet)
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>'
                   r'\d+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', send_confirmation_code, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
