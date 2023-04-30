import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self) -> bool:
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
    
    def __str__(self) -> str:
        return self.question_text
    
    def __repr__(self) -> str:
        return f"Question({self.pk}, '{self.question_text}', {self.pub_date.date()})"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
    
    def __repr__(self) -> str:
        return f"Choice({self.pk}, '{self.choice_text}', {self.vote})"
