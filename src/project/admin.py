from django.contrib import admin
from .models import Project, Milestone, Task, TimelineChange, Comment, Assigment, TaskDescription, TaskFile, Application

# Register your models here.

admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(Task)
admin.site.register(TimelineChange)
admin.site.register(Comment)
admin.site.register(Assigment)
admin.site.register(TaskDescription)
admin.site.register(TaskFile)
admin.site.register(Application)