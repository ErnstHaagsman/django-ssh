from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.
from sshapp.models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions': latest_questions
    }
    return render(request, 'sshapp/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sshapp/detail.html', {
        'question': question
    })


def results(request, question_id):
    format_string = "You're looking at the results of question %s"
    response = str.format(format_string, question_id)
    return HttpResponse(response)


def vote(request, question_id):
    format_string = "You're voting on question %s"
    response = str.format(format_string, question_id)
    return HttpResponse(response)