from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from rest_framework.pagination import PageNumberPagination


class UserPaginator(PageNumberPagination):
    page_size = 20


class User(AbstractUser):
    passport = models.ImageField(upload_to='passports/', null=True, blank=True)
    link = models.CharField(max_length=10)
    groups = models.ManyToManyField(Group, verbose_name='Группы', related_name='custom_user_groups')
    # Добавьте related_name='custom_user_permissions' для избежания конфликта
    user_permissions = models.ManyToManyField(Permission, verbose_name='Права доступа',
                                              related_name='custom_user_permissions')