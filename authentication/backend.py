from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from .tools import hash_text_sha256

class HashEmailBackend(BaseBackend):
    def authenticate(self, request, email, password, **kwargs):
        try:
            user = get_user_model().objects.get(email=hash_text_sha256(email))

        except get_user_model().DoesNotExist:
            return None

        if user and check_password(password, user.password) and user.is_active:
            return user

        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None