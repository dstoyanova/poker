from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .forms import SessionForm
from .models import Session, Vote
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    sessions = Session.objects.all()

    objects = []
    for s in sessions:
        dto = {
            'pk': s.pk,
            'user': s.user,
            'name': s.name,
            'access': s.get_access_display(),
            'cards': s.get_cards_display()
        }
        objects.append(dto)

    return render(request, 'index.html', locals())


def results(request, session_id):
    session = Session.objects.get(pk=session_id)

    return render(request, 'results.html', locals())


def results_ajax(request, session_id):
    session = Session.objects.get(pk=session_id)
    labels = []
    data = []

    cards = session.get_cards_display().split(',')
    for c in cards:
        number_of_votes = Vote.objects.filter(session=session, vote_value=c).count()
        labels.append(c)
        data.append(number_of_votes)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def vote(request, session_id):
    session = Session.objects.get(pk=session_id)
    cards = session.get_cards_display().split(',')

    # Check if this user has already voted
    vote = Vote.objects.filter(session=session, user=request.user).first()

    return render(request, 'vote.html', locals())


@login_required
def save_vote(request, session_id):
    session = Session.objects.get(pk=session_id)

    if request.method == 'POST':
        vote_value = request.POST.get('vote')
        vote = Vote(session=session, user=request.user, vote_value=vote_value)
        vote.save()

        return HttpResponseRedirect('/polls')

    return render(request, 'vote.html', locals())


@login_required
def update_vote(request, vote_id):
    vote = Vote.objects.get(pk=vote_id)

    if request.method == 'POST':
        new_value = request.POST.get('vote')
        vote.vote_value = new_value
        vote.save()

        return HttpResponseRedirect('/polls')

    return render(request, 'vote.html', locals())


@login_required
def create(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)

        form.save()

        return HttpResponseRedirect('/polls')

    form = SessionForm()

    return render(request, 'create.html', locals())


@login_required
def join(request, session_id):
    session = Session.objects.get(pk=session_id)

    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        if session.access_code == access_code:
            return HttpResponseRedirect('/polls/{}/vote/'.format(session_id))

    return render(request, 'access.html', locals())


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/polls')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
