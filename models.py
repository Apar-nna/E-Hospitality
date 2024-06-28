from django.db import models
from django.conf import settings

class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    # Add other fields as needed for patient information

    def __str__(self):
        return f"Patient: {self.user.get_full_name()}"

    def get_medical_records(self):
        return MedicalRecord.objects.filter(patient=self)

    def get_appointments(self):
        return Appointment.objects.filter(patient=self)

class MedicalRecord(models.Model):
    DIAGNOSIS_CHOICES = [
        ('Blood Analysis', (
            ('blood_count', 'Blood Count'),
            ('glucose_tolerance_test', 'Glucose Tolerance Test'),
            ('enzyme_analysis', 'Enzyme Analysis'),
        )),
        ('Angiography', (
            ('cerebral_angiography', 'Cerebral Angiography'),
        )),
        ('Brain Scanning', (
            ('echoencephalography', 'Echoencephalography'),
            ('magnetoencephalography', 'Magnetoencephalography'),
            ('pneumoencephalography', 'Pneumoencephalography'),
        )),
        ('Skin Test', (
            ('patch_test', 'Patch Test'),
            ('schick_test', 'Schick Test'),
            ('tuberculin_test', 'Tuberculin Test'),
        )),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255, choices=DIAGNOSIS_CHOICES)
    medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    treatment_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical record for {self.patient.user.get_full_name()}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    purpose = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient.user.get_full_name()} on {self.appointment_date}"

class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    plan_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Treatment plan for {self.patient.user.get_full_name()}"

# Other models related to doctor's functionalities can be added here as needed.
