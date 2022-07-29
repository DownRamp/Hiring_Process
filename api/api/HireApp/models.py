from django.db import models

# Create your models here.
class Applicants(models.Model):
    ApplicantId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Status = models.IntegerField()
    Flag = models.BooleanField(default=False)

class Jobs(models.Model):
    JobId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)

