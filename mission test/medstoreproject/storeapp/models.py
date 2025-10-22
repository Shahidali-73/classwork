from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.name} (stock: {self.stock})"
