from django.db import models

from company.models import Company


# Create your models here.
class Project:
    pass


class Project(models.Model):
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True,
                                related_name="Project")
    name = models.TextField(blank=True, null=True)
    leader = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} | {self.updated_at}'