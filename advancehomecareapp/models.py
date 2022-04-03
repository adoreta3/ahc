from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    phone = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name