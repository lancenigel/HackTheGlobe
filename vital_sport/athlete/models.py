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
    athlete_image = models.ImageField(
        null=True, upload_to="athletes/")

    def __str__(self):
        return 'Athlete(%s)-Coach(%s)' % (self.id, self.coach.id)
