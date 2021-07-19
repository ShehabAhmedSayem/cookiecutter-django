from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.users.managers import UserManager


USER_NONE = 1
USER_TYPE_CHOICES = [
    (USER_NONE, 'None'),
]
class User(AbstractUser):
    """Default user for {{cookiecutter.project_name}}."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.PositiveSmallIntegerField(_("type of user"), choices=USER_TYPE_CHOICES, default=USER_NONE)
    image = models.ImageField(_("image of user"), upload_to='profile_pic/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"email": self.email})


class LoggedInUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='logged_in_user')
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.email
