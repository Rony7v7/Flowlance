from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(blank=True, max_length=500)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ProjectAvailable(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(blank=True, max_length=500)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_available")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Milestone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default = date.today)
    end_date = models.DateField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="milestones"
    )


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.CharField(max_length=50)
    milestone = models.ForeignKey(
        Milestone,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )

class TimelineChange(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='timeline_changes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.timestamp}"
