from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Contact(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)  # mostrar contato
    picture = models.ImageField(
        blank=True, upload_to="contact_pictures/%Y/%m/%d/"
    )  # imagem do contato
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
