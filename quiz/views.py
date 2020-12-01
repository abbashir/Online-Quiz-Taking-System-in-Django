from django.shortcuts import render
from .models import Subject, Question


# Create your views here.
def home(request):
    subjects = Subject.objects.all()

    return render(request, 'quiz/home.html', {'subjects': subjects})


def takequiz(request):
    if request.method == 'POST':
        candidate_name = request.POST.get('name')
        if request.POST.get('Python'):
            question = Question.objects.filter(id=2)

        return render(request, 'quiz/takequiz.html', {'candidate_name': candidate_name, 'questions': question})
    else:
        pass


def about(request):
    
    return render(request, 'quiz/about.html', {'subjects': subjects})
