from django.db import models
from django.utils import timezone

# Create your models here.
class Services(models.Model):
    service_id = models.CharField(max_length=100, primary_key=True)
    service_name = models.CharField(max_length=100)
    service_price = models.IntegerField()

    def __str__(self):
        return self.service_id

class Caregiver(models.Model):    
    employee_id = models.CharField(max_length=100, primary_key=True)
    employee_name = models.TextField()
    current_address = models.TextField()
    birth_year = models.IntegerField()
    skill_level = models.IntegerField()
    preferred_working_location = models.TextField(null=True)
    working_status = models.CharField(max_length=100, null=True)
    employee_phone = models.CharField(max_length=100, null=True)
    employee_gender = models.CharField(max_length=10)
    national_id = models.CharField(max_length=100)
    national_id_issue_date = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    age = models.IntegerField(default=0)

    def get_age(self):
        return timezone.now().year - self.birth_year
    
    def save(self, *args, **kwargs):
        self.age = int(self.get_age())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id}: {self.employee_name}, {self.age}, {self.skill_level}"


class Customers(models.Model):
    customer_id = models.CharField(max_length=100, primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    source = models.CharField(max_length=100)
    source_reference_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_id

class Patients(models.Model):    
    patient_id = models.CharField(max_length=100, primary_key=True)
    patient_name = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    patient_type = models.CharField(max_length=100)
    physical_condition = models.CharField(max_length=100)
    memory_condition = models.CharField(max_length=100)
    ulcer = models.BooleanField()
    neural_disease = models.BooleanField()
    endo_tube = models.BooleanField()
    nebuliser = models.BooleanField()

    def __str__(self):
        return self.patient_id

class Shifts(models.Model):
    shift_id = models.CharField(max_length=100, primary_key=True)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    customer_id = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Caregiver, on_delete=models.CASCADE)
    rating = models.IntegerField()
    shift_status = models.CharField(max_length=100)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    caring_address = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)
    customer_requirements = models.CharField(max_length=100)

    def __str__(self):
        return self.shift_id
