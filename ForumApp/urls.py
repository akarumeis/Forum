from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', reg_form, name='reg_form'),
    path('login/', log_form, name='log_form'),
    path('forum/', forum, name='forum'),
    path('create_question/', create_question, name='create_question'),
    path('question/<question_pk>', show_question),
]
