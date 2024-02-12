from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')
    jobrole = models.CharField(max_length=100)


class Meta:
        db_table='candidate_details'


