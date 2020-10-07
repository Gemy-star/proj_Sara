from django.urls import path
from . import views

urlpatterns = [
    path('create/exam', views.create_exam, name='create-exam-page'),
    path('create/question', views.create_question, name='create-question-page'),

]
