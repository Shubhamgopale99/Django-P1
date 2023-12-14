from django.db import models


class users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)


class Meta:
    db_table = "users"
# Create your models here.
