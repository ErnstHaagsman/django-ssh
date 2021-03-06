from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse
from django.views import generic

from sshapp.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'sshapp/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'sshapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'sshapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Go back to the form, with an error message
        return render(request, 'sshapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
