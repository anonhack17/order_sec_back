from django.db import models

# Create your models here.
class Company(models.Model):
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    name = models.TextField(blank=True, null=True)
    leader = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} | {self.updated_at}'