from django.shortcuts import render, redirect
from django.contrib import messages

from questions.forms import QuestionForm
from questions.models import Question, Answer, Tag


# Create your views here.
def question_detail_view(request, question_id):
    pass


def question_list_view(request):
    pass


def question_update_view(request, question_id):
    pass


def question_delete_view(request, question_id):
    pass


def question_upvote_view(request, question_id):
    pass


def question_downvote_view(request, question_id):
    pass


def question_create_view(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'question/question_form.html', {'form': form})
    form = QuestionForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return redirect('question_detail', question_id=obj.id)
    return render(request, 'question/question_form.html', {'form': form})


def question_search_view(request):
    pass


def answer_create_view(request, question_id):
    pass


def answer_update_view(request, answer_id):
    pass


def answer_delete_view(request, answer_id):
    pass


def answer_upvote_view(request, answer_id):
    pass


def answer_downvote_view(request, answer_id):
    pass


def tag_list_view(request):
    pass


def tag_create_view(request):
    pass
