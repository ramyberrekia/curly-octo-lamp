from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGen(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        hashed = six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.profile.is_activated)
        return hashed


create_token = TokenGen()