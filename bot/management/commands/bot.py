from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from bot.models import Student, ProjectManager, VacantTime, Team, Project
from bot.db_utils import proposed_times
from bot.utils import get_finish_day
from ProjectsAutomation.settings import CALL_DURATION, ADMIN_TG_CHAT_ID


def choose_time_calling(project):
    # функция рассылки предлагаемого времени ученикам
    students = Student.objects.filter(is_active=True)
    times = [time.strftime("%H:%M") for time in proposed_times()]
    # times раскидать по кнопкам
    # добавить кнопку "нет удобного времени"
    start_day = project.start_day.strftime("%d.%m")
    finish_day = get_finish_day(project.start_day).strftime("%d.%m")
    msg = 'Привет, наступает пора командных проектов. ' \
          'Будет вместо учебного плана.\n' \
          'Будет что-то вроде урока на девмане, только без шагов, ' \
          'зато втроём (очень редко вдвоем) + с ПМом. ' \
          f'Созвоны будут по {CALL_DURATION.seconds // 60} минут ' \
          'каждый день в течение недели. ' \
          'Быть у компьютера не обязательно.\n\n' \
          f'Проект пройдет с {start_day} по {finish_day}.' \
          'Выберите удобное время для созвонов:'
    # разослать ученикам из students
    pass


# @handler
def notify_about_no_good_time():
    # если на запрос из choose_time_calling пользователь нажал "нет удобного времени"
    student = Student.objects.get_object_or_404(id_telegram=message.chat.id)  # message извлекается из ответа
    msg = f'Ученик {student.name} (id={student.id}) ' \
          'не смог найти для себя подходящего свободного времени.\n' \
          'Свяжитесь с ним.'
    # отправить сообщение админу на ADMIN_TG_CHAT_ID
    pass


# @handler
def save_chosen_time():
    # если на запрос из choose_time_calling пользователь выбрал время
    pass


def ask_reschedule_time(message, prop_time, students):
    # функция предлагает выбранным студентам перенести время
    # кнопки да/нет
    pass


# @handler
def notify_about_time_changes():
    # принимает ответ на вопрос из ask_reschedule_time
    # отправляет админу одно из сообщений в тг, в зависимости от ответа 
    pass


class Command(BaseCommand):
    help = 'телеграм бот'

    def handle(self, *args, **kwargs):
        pass