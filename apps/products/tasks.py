import random
from faker import Faker
from celery import shared_task, Celery

from .models import Product
from faker_commerce import Provider

fake = Faker()
fake.add_provider(Provider)


@shared_task
def create_product(name='create product every 5 seconds'):
    for _ in range(10):
      product = Product.objects.create(
        name=fake.ecommerce_name(),
        description=fake.text(),
        price=round(random.uniform(10.0, 100.0), 2))
      print(f"{product.name} has been created")
    return "succesfully created"
