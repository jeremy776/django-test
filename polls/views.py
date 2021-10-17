from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Choice

# Create your views here.

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  list_question = Question.objects.all()
  return render(request, "polls/index.html", { 'list_question': list_question, 'latest_question_list': latest_question_list })
  
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("tidak ada");
  return render(request, "polls/detail.html", { 'question': question })
  
def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)
  
def vote(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("tidak ada")
  try:
    selected_choice = question.choice_set.get(pk=request.POTS["choice"])
  except Choice.DoesNotExist:
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice += 1
    selected_choice.save()
    
  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))