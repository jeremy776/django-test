from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls', namespace="polls")),
    path('admin/', admin.site.urls),
]