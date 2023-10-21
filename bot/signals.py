import json
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from datetime import datetime

from bot.models import Project, ProjectManager, Student, StudyLevel
from bot.management.commands.bot import choose_time_calling


def pm_parsing(pm):
    id_telegram = pm.get('id_telegram')
    name = pm.get('name')
    if not id_telegram or not name:
        return

    time_from = datetime.strptime(pm.get('time_from'), "%H:%M").time()
    time_to = datetime.strptime(pm.get('time_to'), "%H:%M").time()
    is_active = True if time_from and time_to else False

    ProjectManager.objects.update_or_create(
        id_telegram=id_telegram,
        defaults={
            'name': name,
            'time_from': time_from,
            'time_to': time_to,
            'is_active': is_active
        }
    )   


def student_parsing(student):
    id_telegram = student.get('id_telegram')
    name = student.get('name')
    level_id = student.get('level_id')
    if not id_telegram or not name or not level_id:
        return

    try:
        level = get_object_or_404(StudyLevel, id=int(level_id))
        Student.objects.update_or_create(
            id_telegram=id_telegram,
            defaults={
                'name': name,
                'level': level,
                'is_active': True
            }
        )
    except Http404:
        return
    

@receiver(post_save, sender=Project)
def parse_project_files(sender, instance, **kwargs):
    print("parse_project_files запустился")
    if instance.pm_file:
        file_path = instance.pm_file.path
        with open(file_path, 'r', encoding='utf-8') as file:
            pms = json.load(file)
            for pm in pms:
                pm_parsing(pm)

        if instance.students_file:
            file_path = instance.students_file.path
            with open(file_path, 'r', encoding='utf-8') as file:
                students = json.load(file)
                for student in students:
                    student_parsing(student)

        # удалять распарсенные файлы?
        choose_time_calling(instance)
