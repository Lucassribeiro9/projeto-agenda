"""Criando dados com o faker"""
import os
import sys
import django
from datetime import datetime
from pathlib import Path
from random import choice
from django.conf import settings

DJANGO_PROJECT_PATH = Path(__file__).resolve().parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_PROJECT_PATH))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
settings.USE_TZ = False
django.setup()

# Criando dados com o faker
if __name__ == "__main__":
    import faker
    from contact.models import Category, Contact
    
    # Chamando os models
    Contact.objects.all().delete()
    Category.objects.all().delete()
    # Criando categorias
    fake = faker.Faker("pt_BR")
    categories = ["Amigos", "Família", "Trabalho", "Outros"]
    
    django_categories = [Category(name=name) for name in categories]
    
    for category in django_categories:
        category.save()
    # Criando contatos
    django_contacts = []
    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile["mail"]
        first_name = profile["name"].split()[0]
        last_name = profile["name"].split()[-1]
        phone = fake.phone_number()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)
        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                description=description,
                category=category,
            )
        )
    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)