from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256,unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
