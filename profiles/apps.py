from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    App configuration for 'profiles'.

    Attributes:
        default_auto_field (str): the type of primary key for models in this app.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
