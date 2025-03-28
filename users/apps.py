"""App config for users."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User app configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
