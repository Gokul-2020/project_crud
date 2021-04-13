from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender'),
    ('I prefer not to say', 'I prefer not to say'),
)


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name.capitalize()} Profile'
