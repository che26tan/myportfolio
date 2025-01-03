from django.db import models
from django.utils.timezone import now
  
class User(models.Model):
    created_at = models.DateTimeField(default=now) 
    user_name = models.CharField(max_length=100, unique=True)  # Ensure username is unique
    user_password = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)  # Ensure email is unique

    def __str__(self):
        return self.user_name