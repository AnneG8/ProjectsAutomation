from django.contrib import admin
from bot.models import (Project, VacantTime, Team, 
						StudyLevel, Student, ProjectManager)


admin.site.register(Project)
admin.site.register(VacantTime)
admin.site.register(Team)
admin.site.register(StudyLevel)
admin.site.register(Student)
admin.site.register(ProjectManager)
