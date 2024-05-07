from typing import Self
from django.http import HttpRequest, HttpResponse

from gonoshop_auth.models import User


class EmailAuthBackEnd:
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self: Self, request: HttpRequest, username: str = None, password: str = None) -> User | None:
        try:
            user: User = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (Exception):
            return None

    def get_user(self: Self, user_id: int) -> User | None:
        try:
            return User.objects.get(id=user_id)
        except (User.DoesNotExist):
            return None
