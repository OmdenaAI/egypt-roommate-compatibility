from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introvert_extrovert_result = models.CharField(max_length=10, choices=[('Extrovert', 'Extrovert'), ('Introvert', 'Introvert')])
    user_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user_name