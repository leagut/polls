from django.shortcuts import render, redirect
from .models import Poll, Choice, Vote

# Create your views here.
def polls(request):
    polls = Poll.objects.all()
    choices = Choice.objects.all()

    context = {
        'polls': polls,
        'choices': choices,
    }

    return render(request, 'polls/polls.html', context)

def poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    choices = Choice.objects.filter(poll=poll)
    context = {
        'poll': poll,
        'choices': choices,
    }

    if request.method == 'POST':
        choice_id = request.POST.get('option')
        vote = Vote(choice_id=choice_id)
        vote.save()
        return redirect('polls')


    return render(request, 'polls/poll_detail.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    choices = Choice.objects.filter(poll=poll)
    votes = Vote.objects.filter(choice__poll=poll)

    
    context = {
        'poll': poll,
        'choices': choices,
        'votes': votes,
    }

    return render(request, 'polls/poll_total_votes.html', context)