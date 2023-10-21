from bot.models import Student, ProjectManager
from bot.utils import get_end_time
from ProjectsAutomation.settings import CALL_DURATION


def proposed_times(pms: ProjectManager):
    proposed_times = []
    for pm in pms:
        possible_time = pm.time_from
        while possible_time <= pm.time_to:
            if (possible_time not in proposed_times and
                not pm.curr_teams.filter(call_start=possible_time)):
                proposed_times.append(possible_time)
            possible_time = get_end_time(possible_time)
    return proposed_times


def get_choose_time_calling_message(project):
    start_day = project.start_day.strftime("%d.%m")
    finish_day = get_finish_day(project.start_day).strftime("%d.%m")
    return 'Привет, наступает пора командных проектов. ' \
           'Будет вместо учебного плана.\n' \
           'Будет что-то вроде урока на девмане, только без шагов, ' \
           'зато втроём (очень редко вдвоем) + с ПМом. ' \
           f'Созвоны будут по {CALL_DURATION.seconds // 60} минут ' \
           'каждый день в течение недели. ' \
           'Быть у компьютера не обязательно.\n\n' \
           f'Проект пройдет с {start_day} по {finish_day}.' \
           'Выберите удобное время для созвонов:'
