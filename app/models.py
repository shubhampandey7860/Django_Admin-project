from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=50)
    id=models.IntegerField(primary_key=True)
    salary=models.IntegerField()
