from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from .models import User


class UserResource(resources.ModelResource):

    class Meta:
        model = User


class UserAdmin(ImportExportActionModelAdmin):
    resource_class = UserResource


admin.site.register(User, UserAdmin)
