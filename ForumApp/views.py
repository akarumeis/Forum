from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from ForumApp.models import *
# Create your views here.


def reg_form(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        context = {'username': username, 'email': email,
                   'password': password, 'password_confirm': password_confirm}

        if password == password_confirm:
            try:
                User.objects.create_user(
                    username=username, email=email, password=password)
                return redirect('forum')
            except IntegrityError:
                context['error'] = 'Користувач вже існує'
        else:
            context["error"] = "Паролі не спiвпадають"
    return render(request, 'ForumApp/reg_form.html', context)


def log_form(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        context = {'username': username, 'password': password}
        user = authenticate(request, username=username, password=password)

        if user != None:

            login(request, user)
            return redirect('forum')
        else:
            context['error'] = 'Логін або пароль невірні'
    return render(request, 'ForumApp/log_form.html', context)

def forum(request):
    questions = Question.objects.all()
    return render(request, 'ForumApp/forum.html', context={'questions': questions, 'name': 'Forum'})

    
def create_question(request):
    
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            author = request.user.username
            title = request.POST.get('title')
            text = request.POST.get('text')

            Question.objects.create(author=author, title = title, text = text)
            context['success_text'] = 'Ваше запитання створено.' 

        return render(request, 'ForumApp/create_question.html', context = context)
    else:
        return redirect('log_form')

def show_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    
    if request.method == 'POST':
        author = request.user.username
        text = request.POST.get('text')
        Answer.objects.create(author=author, text=text, question_id = question_pk)
    answers = Answer.objects.filter(question_id = question_pk)
    return render(request, 'ForumApp/question.html', context = {'question': question, 'answers': answers})