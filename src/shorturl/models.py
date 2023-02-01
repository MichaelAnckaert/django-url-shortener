from django.db import models


class ShortendUrl(models.Model):
    destination_url = models.CharField(max_length=500)

    def __str__(self):
        return self.destination_url
