from django.shortcuts import render
from bot.models import Student, ProjectManager
from bot.db_utils import proposed_times


def index(request):
    return render(request, 'index.html')


def choose_students(request):
    # students = Student.objects.all()
    # times = proposed_times()
    students = ['Вася', 'Петя', 'Маша']
    times = ['18:00', '18:30', '19:00', '19:30']
    return render(request, 'choose_students.html', context={
        'students': students,
        'times': times,
        'message': 'Удобно ли вам будет созваниваться в '
    })
