import logging

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


logger = logging.getLogger('oc_lettings_site')


class Address(models.Model):
    """
    Model representing the location details.

    Methods:
        __str__(): Returns a string representation of the address.
        save(): Overrides the default save method to log successful saves and errors.

    Meta:
        verbose_name_plural (str): Specifies the plural name for the model
        in the admin interface.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)],
                                         verbose_name="Street number"
                                         )
    street = models.CharField(max_length=64,
                              verbose_name="Street name"
                              )
    city = models.CharField(max_length=64,
                            verbose_name="City name"
                            )
    state = models.CharField(max_length=2,
                             validators=[MinLengthValidator(2)],
                             verbose_name="Two-letter state code"
                             )
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)],
                                           verbose_name="Zip code"
                                           )
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)],
                                        verbose_name="Country iso code"
                                        )

    def __str__(self):
        return f'{self.number} {self.street}'

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            logger.info(f"Address {self} saved successfully")
        except Exception:
            logger.error(f"Error saving address: {self}", exc_info=True)
            raise

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
        save(): Overrides the default save method to log successful saves and errors.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            logger.info(f"Letting '{self.title}' saved successfully")
        except Exception:
            logger.error(f"Error saving letting '{self.title}'", exc_info=True)
            raise
