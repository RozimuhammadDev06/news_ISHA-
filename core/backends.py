from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import make_password

from .models import User


class PhoneBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        if not phone_number or password is None:
            return None
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            # Spend the same hashing work for unknown phone numbers.
            make_password(password)
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        return User.objects.filter(pk=user_id).first()
