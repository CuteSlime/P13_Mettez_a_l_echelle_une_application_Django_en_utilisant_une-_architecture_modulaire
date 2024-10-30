from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing the location details.

    Attributes:
        number (PositiveIntegerField): The building number in the address.
        street (CharField): The street name of the address.
        city (CharField): The city name of the address.
        state (CharField): The two-letter state codes.
        zip_code (PositiveIntegerField): The postal code of the address.
        country_iso_code (CharField): The 3-letter ISO country code.

    Methods:
        __str__(): Returns a string representation of the address.

    Meta:
        verbose_name_plural (str): Specifies the plural name for the model
                                   in the admin interface.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Model representing a letting, using a title and an address.

    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): A one-to-one relationship with the Address model.

    Methods:
        __str__(): Returns a string representation of the letting, using its title.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
