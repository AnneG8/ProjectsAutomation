from django.core.management.base import BaseCommand
from bot.models import Student, ProjectManager, VacantTime, Team


def choose_time_calling():
	# функция рассылки предлагаемого времени ученикам
	pass


def ask_reschedule_time():
	# функция предлагает выбранным студентам перенести время
	pass



class Command(BaseCommand):
    help = 'телеграм бот'

    def handle(self, *args, **kwargs):
    	pass