import datetime

from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from sshapp.models import Question


class QuestionMethodTests(TestCase):
    def test_published_recently_with_future_question(self):
        """
        was_published_recently should return False for questions
        with a pub_date in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
