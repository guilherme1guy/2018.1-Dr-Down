from django.utils.translation import ugettext_lazy as _
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.dates import MonthArchiveView
from drdown.appointments.models import Appointment
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from ..forms.appointments_form import AppointmentSearchForm
from django.utils import timezone
from django.urls import reverse


class AppointmentFilter(BaseFilter):
    search_fields = {
        'search_date': ['date'],
        'search_speciality': ['speciality'],
        'search_doctor': ['doctor__id'],
        'search_patient': ['patient__id'],
    }


class AppointmentListView(SearchListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    form_class = AppointmentSearchForm
    filter_class = AppointmentFilter

    @staticmethod
    def get_list_of_years(request):
        years = []
        for appointment in AppointmentListView.prepare_queryset(request):
            if appointment.date.year not in years:
                years.append(appointment.date.year)
        years.sort(reverse=True)
        return years

    @staticmethod
    def get_list_of_months(request):
        months = []
        for appointment in AppointmentListView.prepare_queryset(request):
            if appointment.date.strftime("%B") not in months:
                months.append(appointment.date.strftime("%B"))
        return months

    @staticmethod
    def prepare_context(context, request):
        context['years'] = AppointmentListView.get_list_of_years(request)
        context['months'] = AppointmentListView.get_list_of_months(request)
        context['current_year'] = timezone.now().year
        return context

    @staticmethod
    def prepare_queryset(request):
        user = request.user
        if hasattr(user, 'patient'):
            queryset = Appointment.objects.filter(
                patient=user.patient
            )
        elif hasattr(user, 'responsible'):
            queryset = Appointment.objects.filter(
                patient=user.responsible.patient
            )
        elif hasattr(user, 'employee'):
            queryset = Appointment.objects.all()
        elif hasattr(user, 'healthteam'):
            queryset = Appointment.objects.filter(
                doctor=user.healthteam
            )
        else:
            queryset = Appointment.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        return self.prepare_context(context, self.request)

    def get_queryset(self):
        return self.prepare_queryset(self.request)


class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = [
        'speciality',
        'shift',
        'doctor',
        'patient',
        'date',
        'time',
        'motive',
    ]

    def get_success_url(self, **kwargs):
        print("Entra em get_success_url")
        success_create_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_create_url

    @staticmethod
    def get_health_team():
        health_team = []

        for doctor in HealthTeam.objects.all():
            health_team.append(doctor)

        return health_team

    @staticmethod
    def get_patients():
        patients = []

        for patient in Patient.objects.all():
            patients.append(patient)

        return patients

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)

        context['health_team'] = self.get_health_team()
        context['patients'] = self.get_patients()
        return context


class AppointmentMonthArchiveView(MonthArchiveView):
    date_field = "date"
    allow_future = True
    template_name = 'appointments/appointment_list.html'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(AppointmentMonthArchiveView,
                        self).get_context_data(**kwargs)
        return AppointmentListView.prepare_context(context, self.request)

    def get_queryset(self):
        return AppointmentListView.prepare_queryset(self.request)


class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['speciality',
              'shift',
              'doctor',
              'patient',
              'date',
              'time',
              'motive', ]

    def get_success_url(self, **kwargs):
        success_update_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_update_url

    def get_object(self):
        appointment = Appointment.objects.get(
            pk=self.kwargs.get('appointment_pk')
        )
        return appointment

    def get_context_data(self, **kwargs):
        context = super(AppointmentUpdateView, self).get_context_data(**kwargs)

        context['health_team'] = AppointmentCreateView.get_health_team()
        context['patients'] = AppointmentCreateView.get_patients()
        return context


class AppointmentUpdateStatusView(UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_cancel.html'
    fields = []

    def get_success_url(self, **kwargs):
        success_update_status_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_update_status_url

    def get_object(self):
        appointment = Appointment.objects.get(
            pk=self.kwargs.get('appointment_pk')
        )
        return appointment

    def form_valid(self, form):
        form.instance.status = _('Canceled')
        form.save()
        return super(AppointmentUpdateStatusView, self).form_valid(form)



