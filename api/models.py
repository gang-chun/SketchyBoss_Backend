from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Actor(models.Model):
    fName = models.CharField(max_length=30, verbose_name='First Name')
    lName = models.CharField(max_length=30, verbose_name='Last Name')
    job_position = models.CharField(max_length=50)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fName + ' ' + self.lName


class Company(models.Model):
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Companies'

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


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
    user = models.ForeignKey('auth.User', default=User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
