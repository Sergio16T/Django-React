from django.shortcuts import HttpResponse


# Create your views here.
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-publish_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# def index(request):
#     return HttpResponse("Hello World. You're at the polls index.")


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    return HttpResponse(f"Detail: You're looking at question {question_id}.")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
