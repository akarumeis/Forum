from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    text = models.TextField()

class Answer(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)