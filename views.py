from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from .forms import AppointmentForm, MedicalRecordForm, BillingForm, PaymentForm, InsuranceForm

from .models import Appointment, MedicalRecord, Billing, Payment, Insurance


def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            if request.user.is_authenticated:
                appointment.patient = request.user
                appointment.save()
                messages.success(request, 'Appointment created successfully.')
                return redirect('patient_dashboard')
            else:
                messages.error(request, 'User is not authenticated.')
        else:
            # Print form errors for debugging
            print(form.errors)
            messages.error(request, 'Error creating appointment. Please check the form.')
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user).order_by('appointment_date', 'appointment_time')

class AppointmentRescheduleView(UpdateView):
    model = Appointment
    template_name = 'reschedule_appointment_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment-list')

    def form_valid(self, form):
        form.instance.status = 'Rescheduled'
        self.object = form.save()
        messages.success(self.request, 'Appointment rescheduled successfully!')
        return super().form_valid(form)
@require_POST
def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient=request.user)
    appointment.status = 'Cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled successfully.')
    return redirect('patient:appointment_list')

class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medical_record_form.html'
    success_url = reverse_lazy('patient:medical-record-list')

    def form_valid(self, form):
        form.instance.patient = self.request.user
        messages.success(self.request, 'Medical record created successfully!')
        return super().form_valid(form)

class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medical_record_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        return MedicalRecord.objects.filter(patient=self.request.user)

class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'medical_record_detail.html'
    context_object_name = 'record'

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medical_record_form.html'
    success_url = reverse_lazy('patient:medical-record-list')

    def form_valid(self, form):
        messages.success(self.request, 'Medical record updated successfully!')
        return super().form_valid(form)

class BillingCreateView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billing_form.html'

    def get_success_url(self):
        return reverse_lazy('patient:payments')

    def form_valid(self, form):
        form.instance.patient = self.request.user
        messages.success(self.request, 'Billing created successfully.')
        return super().form_valid(form)
class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'

    def get_success_url(self):
        return reverse_lazy('patient:payments')  # Redirect to payments page after payment creation

    def form_valid(self, form):
        billing_pk = self.kwargs['pk']
        billing = get_object_or_404(Billing, pk=billing_pk, patient=self.request.user)
        form.instance.billing = billing
        messages.success(self.request, 'Payment made successfully.')
        return super().form_valid(form)

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'
    context_object_name = 'payments'

    def get_queryset(self):
        # Filter payments based on the current user's billings
        return Payment.objects.filter(billing__patient=self.request.user)

class InsuranceCreateView(LoginRequiredMixin, CreateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = 'insurance_form.html'

    def get_success_url(self):
        return reverse_lazy('patient:insurance-detail')

    def form_valid(self, form):
        form.instance.patient = self.request.user
        messages.success(self.request, 'Insurance information created successfully.')
        return super().form_valid(form)

class InsuranceUpdateView(LoginRequiredMixin, UpdateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = 'insurance_form.html'

    def get_object(self):
        return get_object_or_404(Insurance, patient=self.request.user)

    def get_success_url(self):
        return reverse_lazy('patient:insurance-detail')

    def form_valid(self, form):
        messages.success(self.request, 'Insurance information updated successfully.')
        return super().form_valid(form)

class InsuranceDetailView(LoginRequiredMixin, DetailView):
    model = Insurance
    template_name = 'insurance_detail.html'

    def get_object(self):
        return get_object_or_404(Insurance, patient=self.request.user)

