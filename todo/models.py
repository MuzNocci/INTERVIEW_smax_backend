import uuid
from django.db import models



class Task(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    task = models.CharField(max_length=50)


    def __str__(self):

        return self.task