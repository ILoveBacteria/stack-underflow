from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import F

from questions.forms import QuestionForm, AnswerForm, TagForm, SearchForm
from questions.models import Question, Answer, Tag


def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.order_by('-created_at')
    is_up_voted = is_down_voted = False
    if request.user.is_authenticated:
        is_up_voted = question.upvoters.filter(pk=request.user.id).exists()
        is_down_voted = question.downvoters.filter(pk=request.user.id).exists()
    form = AnswerForm()
    context = {'question': question, 'form': form, 'answers': answers, 'is_up_voted': is_up_voted, 'is_down_voted': is_down_voted}
    return render(request, 'question/question_detail_view.html', context)


def question_list_view(request):
    questions = Question.objects.all()
    return render(request, 'question/question_list_view.html', {'questions': questions})


def question_update_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        form = QuestionForm(instance=question)
        return render(request, 'question/question_form.html', {'form': form})
    form = QuestionForm(request.POST, instance=question)
    if form.is_valid():
        obj = form.save()
        return redirect('questions:question_detail', question_id=obj.id)
    return render(request, 'question/question_form.html', {'form': form})


def question_delete_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('questions:question_list')


def question_upvote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.toggle_up_vote(request.user)
    return redirect('questions:question_detail', question_id=question.id)


def question_downvote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.toggle_down_vote(request.user)
    return redirect('questions:question_detail', question_id=question.id)


def question_create_view(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'question/question_form.html', {'form': form})
    form = QuestionForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return redirect('questions:question_detail', question_id=obj.id)
    return render(request, 'question/question_form.html', {'form': form})


def question_search_view(request):
    if request.method == 'GET':
        form = SearchForm()
        return render(request, 'question/question_search.html', {'form': form})
    form = SearchForm(request.POST)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        questions = Question.objects.filter(title__icontains=query)
        return render(request, 'question/question_list.html', {'questions': questions})
    return render(request, 'question/question_search.html', {'form': form})


def answer_create_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        form = AnswerForm()
        return render(request, 'question/question_form.html', {'form': form})
    form = AnswerForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.question = question
        obj.user = request.user
        obj.save()
        return redirect('questions:question_detail', question_id=question_id)
    return render(request, 'question/question_form.html', {'form': form})
    

def answer_update_view(request, answer_id):
    answer = get_object_or_404(Question, pk=answer_id)
    form = AnswerForm(request.POST, instance=answer)
    if form.is_valid():
        obj = form.save()
        return redirect('questions:question_detail', question_id=obj.question.id)
    return render(request, 'question/question_form.html', {'form': form})


def answer_delete_view(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('questions:question_detail', question_id=answer.question.id)


def answer_upvote_view(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.toggle_up_vote(request.user)
    return redirect('questions:question_detail', question_id=answer.question.id)


def answer_downvote_view(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.toggle_down_vote(request.user)
    return redirect('questions:question_detail', question_id=answer.question.id)


def tag_list_view(request):
    tags = Tag.objects.all()
    return render(request, 'tag/tag_list_view.html', {'tags': tags})


def tag_create_view(request):
    if request.method == 'GET':
        form = TagForm()
        return render(request, 'tag/create_tag_form.html', {'form': form})
    form = TagForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return redirect('questions:tag_list')
    return render(request, 'tag/create_tag_form.html', {'form': form})
