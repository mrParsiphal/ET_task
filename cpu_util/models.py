from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CPU_util_input(models.Model):
    ip_address = models.GenericIPAddressField()
    cpu_util = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    date_time = models.DateTimeField(auto_now_add=True)
