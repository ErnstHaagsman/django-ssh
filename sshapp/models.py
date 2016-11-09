import datetime

from django.db import models


# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

    def bump_question(self):
        """Any question older than a day can be bumped to the top"""
        old_post = self.pub_date <= timezone.now() - datetime.timedelta(days=1)
        self.pub_date = timezone.now() if old_post else self.pub_date

        if not old_post:
            raise RuntimeError


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
