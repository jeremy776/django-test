from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    
    # /polls/2
    path("<int:question.id>/", views.detail, name="detail"),
    
    # /polls/2/result
    path("<int:question.id>/results", views.results, name="results"),
    
    # /polls/2/vote
    path("<int:pk>/question.id", views.vote, name="vote")
]