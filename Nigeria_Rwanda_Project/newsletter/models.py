from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Subscribers"