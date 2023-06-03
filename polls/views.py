from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# from django.template import loader
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # latest_question_list = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {
        'latest_question_list': latest_question_list
    }
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist Fucker")
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'polls/detail.html', context)



def results(request, question_id):
    response = "You're looking at the results of question %s %s %d." % (question_id , 564.15, 654)

    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)