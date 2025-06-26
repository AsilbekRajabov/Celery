import logging
from celery import shared_task
from faker import Faker

from .models import Store

fake = Faker()

logger = logging.getLogger(__name__)


@shared_task()
def create_story_every_2_second():
    """"
        Task to create a store every 2 seconds for 10 iterations.
    """

    print("hello mr thompson")
    logger.info("Starting task: create store every 2 seconds")
    for _ in range(10):
        store = Store.objects.create(
            name=fake.name(),
            location=fake.city())
        logger.info(f"{store.name} has been created")

    logger.info("Task completed: create store every 2 seconds")
    return "store successfully created, Mr Thompson"
