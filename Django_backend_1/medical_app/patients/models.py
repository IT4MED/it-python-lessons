from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=20)
    pulse = models.IntegerField()
    temperature = models.FloatField()
