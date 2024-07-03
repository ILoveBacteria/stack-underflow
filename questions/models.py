from django.db import models
from django.urls import reverse

from users.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    upvoters = models.ManyToManyField(User, related_name='question_upvoters')
    downvoters = models.ManyToManyField(User, related_name='question_downvoters')
    tags = models.ManyToManyField(Tag)
    
    @property
    def votes(self):
        return self.upvoters.count() - self.downvoters.count()
    
    def toggle_up_vote(self, user):
        if self.upvoters.filter(pk=user.id).exists():
            self.upvoters.remove(user)
        else:
            self.upvoters.add(user)

    def toggle_down_vote(self, user):
        if self.downvoters.filter(pk=user.id).exists():
            self.downvoters.remove(user)
        else:
            self.downvoters.add(user)


class Answer(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    upvoters = models.ManyToManyField(User, related_name='answer_upvoters')
    downvoters = models.ManyToManyField(User, related_name='answer_downvoters')

    @property
    def votes(self):
        return self.upvoters.count() - self.downvoters.count()
    
    def toggle_up_vote(self, user):
        if self.upvoters.filter(pk=user.id).exists():
            self.upvoters.remove(user)
        else:
            self.upvoters.add(user)

    def toggle_down_vote(self, user):
        if self.downvoters.filter(pk=user.id).exists():
            self.downvoters.remove(user)
        else:
            self.downvoters.add(user)
