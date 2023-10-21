from bot.models import Student, ProjectManager
from bot.utils import get_end_time


def proposed_times():
    proposed_times = []
    for pm in ProjectManager.objects.all():
        possible_time = pm.time_from
        while possible_time <= pm.time_to:
            if possible_time not in proposed_times:
                proposed_times.append(possible_time)
            possible_time = get_end_time(possible_time)
    return proposed_times