from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Court(models.Model):
    name = models.CharField(max_length=20)
    obs = models.TextField()
    available = models.BooleanField(default=True)


class Reservation(models.Model):
    # Hay que colocar el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    start_date = models.DateTimeField('Hora Inicio')
    end_date = models.DateTimeField('Hora Fin')
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



