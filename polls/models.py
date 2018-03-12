from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    # toString
    def __str__(self): return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # custom method
    def was_published_recently(self): return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # toString
    def __str__(self): return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)