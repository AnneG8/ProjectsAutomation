import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime.datetime import strptime

from bot.models import Project, ProjectManager
from bot.management.commands.bot import choose_time_calling


@receiver(post_save, sender=Project)
def parse_project_files(sender, instance, **kwargs):
    if instance.pm_file:
        with open(instance.pm_file.path, 'r') as file:
            pms = json.load(file)

            for pm in pms:
                id_telegram = pm.get('id_telegram')
                name = pm.get('name')
                if not id_telegram or not name:
                    continue

                time_from = strptime(pm.get('time_from'), "%H:%M").time()
                time_to = strptime(pm.get('time_to'), "%H:%M").time()
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
        # распарсить и students_file тоже
        # удалять распарсенные файлы?
        choose_time_calling()
