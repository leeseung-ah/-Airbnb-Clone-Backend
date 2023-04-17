from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = (("male", "Male"),)
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = (("kr", "Korea"),)
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = (("won", "Korean Won"),)
        USD = ("usd", "Doller")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.URLField(blank=True)
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(null=True)
    gender = models.CharField(
        max_length=21,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=16,
        choices=LanguageChoices.choices,
    )
    curreny = models.CharField(
        max_length=21,
        choices=CurrencyChoices.choices,
    )
