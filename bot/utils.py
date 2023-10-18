from datetime import time
from ProjectsAutomation.settings import CALL_DURATION


# что делать, если кол-во часов перевалило за 24?
def get_end_time(start_time: time):
    new_minutes = start_time.minute + CALL_DURATION.seconds // 60
    new_hours = start_time.hour + new_minutes // 60
    return time(int(new_hours % 24), int(new_minutes % 60))


# Добавить функцию перерасчета на дальневосточное время (+7ч от МСК)

