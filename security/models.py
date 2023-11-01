from django.db import models
from project.models import Project


# Create your models here.
class Policy(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="policy")
    title = models.CharField(max_length=200)
    content = models.TextField()  # Используем TextField для богатого текста

    def __str__(self):
        return self.title


class Standard(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="standard")
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Procedure(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="procedure")
    title = models.CharField(null=True, blank=True,max_length=200)
    description = models.TextField(null=True, blank=True)
    attribute_name = models.CharField(null=True, blank=True,max_length=100)
    attribute_value = models.CharField(null=True, blank=True,max_length=200)

    def __str__(self):
        return self.title


class BypassSheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="bpassSheet")
    title = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bypass Sheet - {self.title}"

    class Meta:
        verbose_name = 'Расписание аудита'
        verbose_name_plural = 'Расписание аудитов'


class BypassSheetField(models.Model):
    name = models.CharField(max_length=100)
    bypass_sheet = models.ForeignKey(BypassSheet, on_delete=models.CASCADE, related_name="bypass_sheet_field")

    def __str__(self):
        return self.name
