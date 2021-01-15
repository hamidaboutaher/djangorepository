from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    meetingagenda=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class Minutes(models.Model):
    minutesname=models.CharField(max_length=255)
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return self.minutesname
    
    class Meta:
        db_table='minutes'

class resouce(models.Model):
    resoucename=models.CharField(max_length=255)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    dateentered=models.DateField()
    resourceurl = models.URLField()
    resourcedescription= models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'



        
