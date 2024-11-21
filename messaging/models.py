from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
