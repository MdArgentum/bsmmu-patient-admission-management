from django.db import models

# Create your models here.

class Patient(models.Model):
    """Model definition for Patient."""

    # TODO: Define fields here
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('admited', 'Admited'),
        ('released', 'Released'),
    ]
    patient_id = models.CharField(max_length=50, unique=True, verbose_name='Enter Patiend ID')
    center = models.CharField(max_length=50, blank=True, verbose_name='Center for Patient')
    department = models.CharField(max_length=50, blank=True, verbose_name='Enter Patiend Department Name')
    word = models.CharField(max_length=50, blank=True, verbose_name='Patient Word')
    bed = models.CharField(max_length=50, blank=True, verbose_name='Patient Bed')
    regi_no = models.CharField(max_length=50, unique=True, verbose_name='Patiend Registration Number')
    time = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50, verbose_name='Patient Name')
    age = models.CharField(max_length=50, blank=True, verbose_name='Patient Age')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, verbose_name='Patient Gender')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='admited')
    father_or_husband = models.CharField(max_length=50, blank=True, verbose_name='Patient Father or Husband Name')
    mother = models.CharField(max_length=50, blank=True, verbose_name='Patient Mother Name')
    mailing_address = models.CharField(max_length=250, blank=True, verbose_name='Patient Present Address')
    permanent_address = models.CharField(max_length=250, blank=True, verbose_name='Patient Permanent Address')
    phone = models.CharField(max_length=15, blank=False, verbose_name='Patient Phone Number')
    contact_person = models.CharField(max_length=50, blank=True, verbose_name='Contact Person Name of Patient')
    contact_person_phone = models.CharField(max_length=15, blank=True, verbose_name='Contact Person Phone Number of Patient')

    con_doctor = models.CharField(max_length=50, verbose_name='Consaltant Doctor Name')
    con_doctor_depart = models.CharField(max_length=50, blank=True, verbose_name='Consaltant Doctor Department')
    con_doctor_unit = models.CharField(max_length=50, blank=True, verbose_name='Consaltant Doctor Phone Number')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Patient."""

        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        """Unicode representation of Patient."""
        return self.name


class Contact(models.Model):
    """Model definition for Contact."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.name
