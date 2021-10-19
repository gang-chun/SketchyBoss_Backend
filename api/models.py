from django.db import models
from django.utils import timezone

# Create your models here.


class Actor(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    job_position = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)


class ActorEmployment(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


class Report(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()
