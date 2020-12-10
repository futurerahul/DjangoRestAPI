from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Snippet(models.Model):
    LANGUAGE_CHOICES=[
        ('python', 'Python'),
        ('java', 'Java'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('javascript', 'Javascript'),
    ]
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets', default=1)
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    code=models.TextField()
    line_nos=models.BooleanField(default=True)
    language=models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    class Meta:
        ordering=['created']

    def __str__(self):
        return self.title
