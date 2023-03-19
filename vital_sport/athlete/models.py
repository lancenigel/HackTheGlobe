from django.db import models
from coach.models import Coach


class Athlete(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    ETHNICITY_CHOICES = [
        ('White', 'White'),
        ('Black', 'Black'),
        ('Asian', 'Asian'),
        ('Hispanic', 'Hispanic'),
        ('Other', 'Other')
    ]
    ethnicity = models.CharField(
        max_length=20, choices=ETHNICITY_CHOICES, blank=True)
    sex = models.CharField(max_length=1, choices=(
        ('M', 'Male'), ('F', 'Female')))
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    BLOOD_TYPE_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    blood_type = models.CharField(
        max_length=4, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    sport = models.CharField(max_length=50)
    PHONE = 'phone'
    EMAIL = 'email'
    CONTACT_CHOICES = [
        (PHONE, 'Phone'),
        (EMAIL, 'Email'),
    ]
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField()
    contact_method = models.CharField(
        max_length=5, choices=CONTACT_CHOICES, default=PHONE)

    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, related_name='coach')
    athlete_image = models.URLField()

    def __str__(self):
        return 'Athlete(%s)-Coach(%s)' % (self.id, self.coach.id)
