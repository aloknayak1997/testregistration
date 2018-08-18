from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25)
    mob_no = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user'
