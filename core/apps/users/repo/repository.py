# from dataclasses import dataclass

from rest_framework.generics import get_object_or_404

from core.apps.users.api.serializers import UserCrudSerializer
from core.apps.users.models import User
from core.apps.users.repo.interface import BaseUser
from core.apps.users.services.email import is_valid_email


class UserRepository(BaseUser):

    def get_all() -> list[dict]:
        users_list = User.objects.values(
            'id',
            'username',
            'first_name',
            'last_name',
            'link',
            'email',
        )
        return users_list

    def post(request) -> dict[str]:
        if is_valid_email(request.data['email']):

            serializer = UserCrudSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            return {
                'username': request.data['username'],
                'fist_name': request.data['first_name'],
                'last_name': request.data['last_name'],
                'link': request.data['link'],
                'email': request.data['email'],
            }
        return

    def update(request) -> dict[str]:
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id)
        serializer = UserCrudSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {'id': user.id,
                'username': user.username,
                'fist_name': user.first_name,
                'last_name': user.last_name,
                'link': user.link,
                'email': user.email,
                }

    def delete(self, request) -> dict[str]:
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id)
        user.delete()

        return {'id': user.id,
                'username': user.username,
                'fist_name': user.first_name,
                'last_name': user.last_name,
                'link': user.link,
                'email': user.email,
                }