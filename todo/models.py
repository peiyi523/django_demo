from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_complated = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}-{self.title}-{self.created}"
