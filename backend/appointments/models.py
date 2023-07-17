from django.db import models
from authentication.models import User
from petprofiles.models import PetProfile

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.ForeignKey(PetProfile)
    reason = models.CharField(max_length=255)
    appt_date = models.DateField(max_length=255)
    start = models.TimeField()
    end = models.TimeField()
    vet_name = models.CharField(max_length=255)

