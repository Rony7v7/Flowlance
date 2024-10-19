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
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_projects")
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="projects")
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title


class Milestone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="milestones"
    )
    is_deleted = models.BooleanField(default=False, null=False)

    @property
    def deadline_color(self):
        days_remaining = (self.end_date - date.today()).days
        if days_remaining <= 0:
            return "bg-red-600"
        elif days_remaining <= 3:
            return "bg-red-400"
        else:
            return "bg-green-500"

    def __str__(self):
        return self.name 

    @property
    def amount_completed(self):
        total_deliverables = self.assigments.count()
        if total_deliverables == 0:
            return 0  # Avoid division by zero if there are no deliverables
        completed_deliverables = self.assigments.filter(state='COMPLETADO').count()
        return completed_deliverables


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    responsible = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks"
    )  
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    priority = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    milestone = models.ForeignKey(
        Milestone,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title 


class TimelineChange(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="timeline_changes"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"{self.project.title} - {self.timestamp}"

    @property
    def deadline_color(self):
        days_remaining = (self.end_date - date.today()).days
        if days_remaining <= 0:
            return "bg-red-600"
        elif days_remaining <= 3:
            return "bg-red-400"
        else:
            return "bg-green-500"
        

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"

class Assigment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigments_created"
    )
    responsible = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigments_tasked" 
    )
    milestone = models.ForeignKey(
        Milestone, on_delete=models.CASCADE, related_name="assigments"
    )
    description = models.TextField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    state = models.CharField(max_length=50,default="INICIADO")
    file = models.FileField(null = True , blank= True)
    is_deleted = models.BooleanField(default=False, null=False)

class TaskDescription(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='descriptions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Description by {self.user.username} on {self.task.title}"


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='task_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"File for {self.task.title}"
    
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, default='Pendiente')  
    applied_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=50) 
    is_deleted = models.BooleanField(default=False, null=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.project.title} ({self.status})"

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="events")
    reminder_time = models.CharField(max_length=50, null=True, blank=True)  

    def __str__(self):
        return self.name
