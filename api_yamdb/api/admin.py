from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from reviews.models import Category, Comment, Genre, Review, Title, TitleGenre


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class TitleGenreResource(resources.ModelResource):
    class Meta:
        model = TitleGenre
        fields = (
            'id',
            'title_id',
            'genre_id'
        )


class ReviewResource(resources.ModelResource):
    title = Field(attribute='title', column_name='title_id',
                  widget=ForeignKeyWidget(Title)
                  )

    class Meta:
        model = Review


class GenreAdmin(ImportExportActionModelAdmin):
    resource_class = GenreResource


class CommentAdmin(ImportExportActionModelAdmin):
    resource_class = CommentResource


class TitleAdmin(ImportExportActionModelAdmin):
    resource_class = TitleResource


class CategoryAdmin(ImportExportActionModelAdmin):
    resource_class = CategoryResource


class TitleGenreAdmin(ImportExportActionModelAdmin):
    resource_class = TitleGenreResource


class ReviewAdmin(ImportExportActionModelAdmin):
    resource_class = ReviewResource


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TitleGenre, TitleGenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
