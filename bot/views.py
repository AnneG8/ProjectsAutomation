from django.shortcuts import render
from django.shortcuts import redirect
from bot.models import Student, ProjectManager
from bot.db_utils import proposed_times
from bot.management.commands.bot import ask_reschedule_time


def index(request):
    return render(request, 'index.html')


def choose_students(request):
    students = Student.objects.filter(is_active=True)
    times = [time.strftime("%H:%M") for time in proposed_times()]
    # students = ['Вася', 'Петя', 'Маша']
    # times = ['18:00', '18:30', '19:00', '19:30']
    return render(request, 'choose_students.html', context={
        'students': students,
        'times': times,
        'message': 'Удобно ли вам будет созваниваться в '
    })


def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        selected_time = request.POST.get('time')
        selected_students = request.POST.getlist('students')
        ask_reschedule_time(message, selected_time, selected_students)
        context = {'message': 'Сообщения отправлены'}
        return render(request, 'index.html', context)
    return redirect('index')