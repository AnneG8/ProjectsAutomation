from django.shortcuts import render
from bot.models import Student, ProjectManager
from bot.db_utils import proposed_times
from django.shortcuts import redirect


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


def send_message(request):
    if request.method == 'POST':
        # for key, value in request.POST.items():
        #     print(f'Ключ: {key}, Значение: {value}')
        selected_time = request.POST.get('time')
        selected_users = request.POST.getlist('students')
        print('Вывод: ', selected_time, selected_users)
        message = "Сообщения отправлены"
        return render(request, 'index.html', {'message': message})
    return redirect('index')