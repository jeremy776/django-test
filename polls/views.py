from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  return render(request, "polls/index.html", { latest_question_list: latest_question_list })
  
def detail(request, question_id):
  question = Question.objects.get(pk=question_id)
  print(question.id)
  print("==============")
  print(question.question_text)
  return render(request, "polls/detail.html", { question: question })
  
def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question.id)
  
def vote(request, question_id):
  return HttpResponse("You're voting for question %s." % question_id)