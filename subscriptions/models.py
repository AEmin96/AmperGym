from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Subscriptions(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.created_at}"