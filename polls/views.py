from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()

    return render(request, 'polls/index.html', {
        'questions': questions
    })

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Requested poll does not exist.")

    return render(request, 'polls/detail.html', {
        'question': question
    })

def result(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Result for the requested poll does not exist.")

    return render(request, 'polls/result.html', {
        'question': question
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        raise Http404("Selected choice does not exist for this question.")
    
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    