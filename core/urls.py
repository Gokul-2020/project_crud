from django.urls import path
from .views import (createPatient, patientDetails, updatePatient,
                    deletePatient, listPatient, getPatientsList)


urlpatterns = [
    # path('', views.home, name="Blog-home"),
    path('add/', createPatient, name="add-patient"),
    path('detail/', patientDetails, name="patient-details"),
    path('edit/', updatePatient, name="update-patient"),
    path('deletePatient/', deletePatient, name="delete-patient"),
    path('view/', listPatient, name="list-patient"),
    path('ajax_view/', getPatientsList, name="ajax-list-patient"),
]
