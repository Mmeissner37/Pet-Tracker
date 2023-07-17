from django.db import models

# Create your models here.

class Medication(models.Model):
    med_name = models.CharField(max_length=255)
    med_dose = models.CharField(max_length=255)
    med_instr = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.med_name}"

