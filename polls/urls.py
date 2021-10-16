from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    
    # /polls/2
    path("<int:pk>/", views.detail, name="detail"),
    
    # /polls/2/result
    path("<int:pk>/results", views.results, name="results"),
    
    # /polls/2/vote
    path("<int:pk>/vote", views.vote, name="vote")
]