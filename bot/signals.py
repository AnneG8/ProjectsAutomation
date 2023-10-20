import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

from bot.models import Project, ProjectManager
from bot.management.commands.bot import choose_time_calling


@receiver(post_save, sender=Project)
def parse_project_files(sender, instance, **kwargs):
    if instance.pm_file:
        with open(instance.pm_file.path, 'r') as file:
            pms = json.load(file)

            for pm in pms:
                time_from = datetime.strptime(
                    pm.get('time_from'), 
                    "%H:%M"
                ).time()
                time_to = datetime.strptime(
                    pm.get('time_to'), 
                    "%H:%M"
                ).time()

                ProjectManager.objects.update_or_create(
                    id_telegram=pm.get('id_telegram'),
                    defaults={
                        'name': pm.get('name'),
                        'time_from': time_from,
                        'time_to': time_to
                    }
                )
        # распарсить и students_file тоже
        # удалять распарсенные файлы?
        choose_time_calling()
