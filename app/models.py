from django.db import models
from django.utils import timezone

# Create your models here.

class Lead(models.Model):
    address = models.CharField(max_length=50)
    buisness_name = models.CharField(max_length=50)
    person_name = models.CharField(max_length=50)
    contact = models.IntegerField()
    v_choice = (('verified', 'Verified'), ('notverified', 'Notverified'))
    verified_status = models.CharField(max_length=50, choices=v_choice, default='notverified')
    time_stamp = models.DateTimeField(default=timezone.now())


from django.db import models

# Create your models here.
