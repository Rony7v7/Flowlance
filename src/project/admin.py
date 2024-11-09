from django.contrib import admin
from .models import Project, Milestone, Task, TimelineChange, Comment, Assigment, TaskDescription, Application, Event, ProjectMember

# Register your models here.

admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(Task)
admin.site.register(TimelineChange)
admin.site.register(Comment)
admin.site.register(Assigment)
admin.site.register(TaskDescription)
admin.site.register(Application)
admin.site.register(Event)
admin.site.register(ProjectMember)