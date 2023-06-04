from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
# from django.template import loader
# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # latest_question_list = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    # return render(request, 'polls/index.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    # try:
    # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist Fucker")
    # return HttpResponse("You're looking at question %s." % question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # context = {'question':question}
    # return render(request, 'polls/detail.html', context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    # question = get_object_or_404(Question, pk = question_id)
    # context = {
    #     'question': question
    # }
    # return render(request, 'polls/result.html', context)
    # response = "You're looking at the results of question %s." % question_id

    # return HttpResponse(response)


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {"question": question,"error_message": "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return render(request, 'polls/result.html', context = {'question_id':question_id} )
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)