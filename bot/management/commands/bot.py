from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from bot.models import Student, ProjectManager, VacantTime, Team, StudyLevel
from bot.db_utils import proposed_times, get_choose_time_calling_message
from bot.utils import get_finish_day
from ProjectsAutomation.settings import (
    ADMIN_TG_CHAT_ID,
    TG_BOT_TOKEN
)


def form_blanks_vacant_time(project):
    # очистить сначала VacantTime? Team? Project кроме project?
    pms = ProjectManager.objects.filter(is_active=True)
    times = proposed_times(pms)
    for time in times:
        curr_pms = pms.filter(time_from__gte=time, time_to__lte=time)
        VacantTime.objects.create(
            call_start=time,
            project=project,
            pms=curr_pms
        )


def choose_time_calling(project):
    # функция рассылки предлагаемого времени ученикам
    form_blanks_vacant_time(project)
    students = Student.objects.filter(is_active=True)
    pms = ProjectManager.objects.filter(is_active=True)
    times = [time.strftime("%H:%M") for time in proposed_times(pms)]

    # times раскидать по кнопкам
    # добавить кнопку "нет удобного времени"

    msg = get_choose_time_calling_message(project)
    # разослать ученикам из students


# @handler
def notify_about_no_good_time():
    # если на запрос из choose_time_calling пользователь нажал "нет удобного времени"
    student = get_object_or_404(Student, id_telegram=message.chat.id)  # message извлекается из ответа
    msg = f'Ученик {student.name} (id={student.id}) ' \
          'не смог найти для себя подходящего свободного времени.\n' \
          'Свяжитесь с ним.'
    # отправить сообщение админу на ADMIN_TG_CHAT_ID


# @handler
def save_chosen_time():
    # если на запрос из choose_time_calling пользователь выбрал время
    chosen_time = datetime.strptime('извлечь время из кнопки', "%H:%M").time()
    student = get_object_or_404(Student, id_telegram=message.chat.id)  # message извлекается из ответа
    vacant_time = get_object_or_404(VacantTime, call_start=chosen_time)
    
    available_pms = vacant_time.available_pms()

    if not available_pms:
        times = [time.strftime("%H:%M") for time in proposed_times(pms)]
        # выслать запрос с извинениями и оставшимися доступными временами повторно
        return

    student.chosen_time = chosen_time
    student.call_time = vacant_time
    student.save()

    for level in StudyLevel.objects.all():
        if vacant_time.students.filter(level=level).count() == 3:
            chosen_students = vacant_time.students.all()[:3]
            chosen_pm = available_pms.first()
            team = Team.objects.create(
                #title=get_team_title()
                project=vacant_time.project,
                pm=chosen_pm,
                call_start=chosen_time
            )
            team.students.set(chosen_students)
            for chosen_student in chosen_students:
                chosen_student.call_time = None
                student.save()




def ask_reschedule_time(message, prop_time, students):
    # функция предлагает выбранным студентам перенести время
    # кнопки да/нет
    pass


# @handler
def notify_about_time_changes():
    # принимает ответ на вопрос из ask_reschedule_time
    # отправляет админу на ADMIN_TG_CHAT_ID одно из сообщений, в зависимости от ответа 
    pass


class Command(BaseCommand):
    help = 'телеграм бот'

    def handle(self, *args, **kwargs):
        pass