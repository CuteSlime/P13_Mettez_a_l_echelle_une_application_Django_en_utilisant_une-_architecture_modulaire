from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile with additional attributes linked to a User account.

    Attributes:
        user (OneToOneField): A one-to-one relationship with Django's built-in User model.
        favorite_city (CharField): An optional field allowing the user to specify a favorite city.

    Methods:
        __str__(): Returns the username associated with the profile for easy identification.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
