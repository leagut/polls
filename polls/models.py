from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def get_choices(self):
        return Choice.objects.filter(poll=self)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option

    def get_votes(self):
        return Vote.objects.filter(choice=self).count()


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice.option