from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    App configuration for 'lettings'.

    Attributes:
        default_auto_field (str): the type of primary key for models in this app.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
