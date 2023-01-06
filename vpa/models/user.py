from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True, default=1, blank=True)
    username = models.CharField(max_length=50, default='GOAT', blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)