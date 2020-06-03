from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager.
    """

    def create(self, email, password, **fields):
        """
        Create and save a User.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **fields):
        """
        Create and save a Normal User.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if fields.get('is_superuser') is True:
            raise ValueError(
                _('Normal user cannot be a super user.')
            )
        return self.create(email, password, **fields)

    def create_superuser(self, email, password, **fields):
        """
        Create and save a Super User.
        """
        fields.setdefault('is_superuser', True)

        if fields.get('is_superuser') is not True:
            raise ValueError(_(
                'Super user must have super_user set to True'
            ))
        return self.create(email, password, **fields)

    def get_by_id(self, id=None):
        """
        Get a user by ID
        """
        if not id:
            raise ValueError(_('An ID is required'))

        return self.get(pk=id)
