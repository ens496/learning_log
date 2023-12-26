from django.shortcuts import render, redirect
from django.urls import path

from . import views
from .forms import TopicForm
from .models import Topic
app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST' :       #Veri gönderilmedi; boş form oluşturur.
        form = TopicForm()
    else:                              #POST verisi gönderildi, veriyi işle
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owmer = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
     #boş veya geçersiz formu görüntüle
    context = {'form': form}
    return render(request, '^learning_logs/new_topic.html', context)

