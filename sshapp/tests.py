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

    def test_can_bump_old_question(self):
        """
        You should be able to bump old questions
        """
        # arrange
        time = timezone.now() - datetime.timedelta(days=2)
        old_question = Question(pub_date=time)

        # act
        old_question.bump_question()

        # assert
        self.assertGreaterEqual(old_question.pub_date, timezone.now() - datetime.timedelta(seconds=1))